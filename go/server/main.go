package main

import (
	"fmt"
	todo_pb "vivek-blip187/gRPC_demo/go/protos"
)

func main() {
	fmt.Println("Charles")
	a := todo_pb.TodoItem{
		Id:   1,
		Text: "Drink",
	}
	fmt.Println(a)
}
