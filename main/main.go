package main

import (
	"coding/payroll/calc"
	"fmt"
)

func main() {
	var salaryamount = 5000.00
	cpp := calc.Cppcalc(salaryamount)
	fmt.Println(cpp)

}
