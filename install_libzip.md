# requires new cmake than the default of rhel7 or centos7
- mkdir build
- cd build
- ccmake ..
  - if `error: unknown type name ‘gnutls_cipher_alggorithm_t’` happens,  -DENABLE_GNUTLS=OFF from cmake menu
- make -j 20; make install
