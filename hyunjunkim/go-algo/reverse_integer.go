package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	var sign = 1
	if x < 0 {
		sign := -1
		x *= sign
	}

	result := 0
	for x > 0 {
		remainder := x % 10
		result *= 10
		result += remainder
		x /= 10
	}
	value := result * sign
        if value > math.MaxInt32 || value < math.MinInt32 {
               return 0
        }
	return value
}
func main() {
	fmt.Println(reverse(0))
}
