FROM samloh84/oracle-java-jdk:7u80-b15-centos7
ARG VENDOR=apache
ARG PRODUCT=maven
ARG PRODUCT_VERSION=3.5.0
ARG TEMP_DIR_ROOT=/tmp/${VENDOR}-${PRODUCT}
ARG TEMP_DIR=/${TEMP_DIR_ROOT}/${PRODUCT_VERSION}
ARG INSTALL_DIR_ROOT=/opt/${VENDOR}-${PRODUCT}
ARG INSTALL_DIR=${INSTALL_DIR_ROOT}/${PRODUCT_VERSION}

ARG APACHE_MAVEN_BINARIES_URL="http://www-eu.apache.org/dist/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz"
ARG APACHE_MAVEN_BINARIES="apache-maven-3.5.0-bin.tar.gz"
ARG APACHE_MAVEN_GPG_KEYS_URL=http://www-eu.apache.org/dist/maven/KEYS
ARG APACHE_MAVEN_GPG_KEYS=KEYS
ARG APACHE_MAVEN_SIGNATURE_URL="http://www-eu.apache.org/dist/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz.asc"
ARG APACHE_MAVEN_SIGNATURE="apache-maven-3.5.0-bin.tar.gz.asc"

USER ${ROOT_UID}

RUN \
mkdir -p ${TEMP_DIR} ${INSTALL_DIR} && \
cd ${TEMP_DIR} && \
curl -LjSs ${APACHE_MAVEN_BINARIES_URL} -o ${APACHE_MAVEN_BINARIES} && \
curl -LjSs ${APACHE_MAVEN_GPG_KEYS_URL} -o ${APACHE_MAVEN_GPG_KEYS} && \
curl -LjSs ${APACHE_MAVEN_SIGNATURE_URL} -o ${APACHE_MAVEN_SIGNATURE} && \
gpg --import ${APACHE_MAVEN_GPG_KEYS} && \
curl -LjSs ${APACHE_MAVEN_SIGNATURE_URL} -o ${APACHE_MAVEN_SIGNATURE} && \
gpg --verify ${APACHE_MAVEN_SIGNATURE} && \
tar -xf ${APACHE_MAVEN_BINARIES} --strip-components=1 -C ${INSTALL_DIR} && \
fix-ownership ${INSTALL_DIR} && \
fix-permissions ${INSTALL_DIR} && \
rm -rf ${TEMP_DIR_ROOT}

ENV M2_HOME ${INSTALL_DIR}
ENV PATH ${M2_HOME}/bin:${PATH}

USER ${APP_UID}
