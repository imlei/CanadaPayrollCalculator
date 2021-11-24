package calc

func Cppcalc(amount float64) float64 {
	cpprate := 0.0195
	cppamt := amount * cpprate
	return cppamt
}

func Eicalc(amount float64) float64 {
	eirate := 0.02
	eiamt := amount * eirate
	return eiamt
}
