.PHONY: test check clean build dist all

check:
	protoc --version

out:
	if [ ! -d "../proto_py" ]; \
	then mkdir -p ../proto_py ; \
	fi
	protoc --python_out=../proto_py ./*.proto