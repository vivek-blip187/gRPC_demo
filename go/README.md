protoc --go_out=. 

go install google.golang.org/protobuf/cmd/protoc-gen-go@latest


protoc --go_out=.  --go-grpc_out=.  todo.proto