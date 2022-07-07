package main

import (

	"log"
	"context"

	"google.golang.org/grpc"
	"github.com/bvisonl/grpc-greeter-test/greeter"
)


func main() {

	conn, err := grpc.Dial(":50051", grpc.WithInsecure())

	if err != nil {
		log.Fatalln("Unable to dial gRPC server:", err)
	}

	defer conn.Close()

	client := greeter.NewGreeterServiceClient(conn)

	response, err := client.SayHello(context.Background(), &greeter.HelloRequest{Name: "World"})

	if err != nil {
		log.Fatalln("Unable to call SayHello:", err)
	}

	log.Println("Response:", response.Message)

}
