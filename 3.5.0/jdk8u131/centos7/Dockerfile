FROM samloh84/oracle-jdk:8u131-centos7

ARG VENDOR=apache
ARG PRODUCT=maven
ARG PRODUCT_VERSION=3.5.0
ARG TEMP_DIR_ROOT=/tmp/${VENDOR}-${PRODUCT}
ARG TEMP_DIR=${TEMP_DIR_ROOT}/${PRODUCT_VERSION}
ARG INSTALL_DIR_ROOT=/opt/${VENDOR}-${PRODUCT}
ARG INSTALL_DIR=${INSTALL_DIR_ROOT}/${PRODUCT_VERSION}

ARG MAVEN_INSTALL_TAR_GZ_URL="http://www-eu.apache.org/dist/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz"
ARG MAVEN_INSTALL_TAR_GZ=apache-maven-3.5.0-bin.tar.gz
ARG MAVEN_INSTALL_TAR_GZ_MD5SUM=35c39251d2af99b6624d40d801f6ff02

ARG MAVEN_KEYS_URL="https://www.apache.org/dist/maven/KEYS"
ARG MAVEN_INSTALL_TAR_GZ_ASC_URL="https://www.apache.org/dist/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz.asc"
ARG MAVEN_INSTALL_TAR_GZ_ASC=apache-maven-3.5.0-bin.tar.gz.asc

USER ${ROOT_UID}

RUN \
mkdir -p ${TEMP_DIR} && \
mkdir -p ${INSTALL_DIR} && \
pushd ${TEMP_DIR} && \
curl -LjSs ${MAVEN_KEYS_URL} -o KEYS && \
curl -LjSs ${MAVEN_INSTALL_TAR_GZ_ASC_URL} -o ${MAVEN_INSTALL_TAR_GZ_ASC} && \
curl -LjSs ${MAVEN_INSTALL_TAR_GZ_URL} -o ${MAVEN_INSTALL_TAR_GZ} && \
gpg --import ./KEYS && \
gpg --verify ${MAVEN_INSTALL_TAR_GZ_ASC} ${MAVEN_INSTALL_TAR_GZ} && \
echo "${MAVEN_INSTALL_TAR_GZ_MD5SUM}  ${MAVEN_INSTALL_TAR_GZ}" | md5sum -c - && \
tar -xzf ${TEMP_DIR}/${MAVEN_INSTALL_TAR_GZ} --strip-components=1 -C ${INSTALL_DIR} && \
fix-ownership ${INSTALL_DIR} && \
fix-permissions ${INSTALL_DIR} && \
popd && \
rm -rf ${TEMP_DIR_ROOT}

ENV M2_HOME ${INSTALL_DIR}
ENV PATH ${PATH}:${M2_HOME}/bin

USER ${APP_UID}
