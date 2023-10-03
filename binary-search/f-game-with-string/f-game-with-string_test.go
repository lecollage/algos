package main

import "testing"

func TestDoesInclude(t *testing.T) {
	str1 := "assd"
	str2 := "ad"
	result := doesInclude(str1, str2)
	if !result {
		t.Errorf("Result was incorrect, got: %s, want: %s.", result, true)
	}

	return
}
