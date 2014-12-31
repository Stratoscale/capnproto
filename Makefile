all: configure build install

ifeq ($(V),1)
  Q =
  QCMAKE = "VERBOSE=1"
else
  Q = @
  QCMAKE =
endif

.PHONY: configure
configure:
	$(Q)mkdir -p build
	$(Q)cd build && cmake -DCMAKE_INSTALL_PREFIX="install" -DBUILD_TESTING:BOOL=OFF ../c++
                                                                                                                                                                                                                                                                                                                  
.PHONY: configure
build: configure
	$(Q)$(MAKE) -C build $(QCMAKE)

.PHONY: install
install: build
	$(Q)$(MAKE) -C build install $(QCMAKE)

.PHONY: submit
submit: rpm
	$(Q)solvent submitproduct rpm build/rpm

.PHONY: clean
clean:
	$(Q)rm -fr build/install
	$(Q)$(MAKE) -C build clean $(QCMAKE)

.PHONY: rpm
rpm: install
	@echo "RPM	" $@
	$(Q)rm -fr build/rpm
	$(Q)mkdir -p build/rpm
	echo "TOP `pwd`"
	$(Q)rpmbuild -ba -vv --define "TOP `pwd`" capnproto.spec $(SWALLOW_STDOUT)
	$(Q)cp $(HOME)/rpmbuild/$*/RPMS/x86_64/*.rpm  build/rpm
	$(Q)cp $(HOME)/rpmbuild/$*/SRPMS/*.rpm  build/rpm
	$(Q)rm build/rpm/*.src.rpm
	$(Q)rm -rf $(HOME)/rpmbuild/$*
