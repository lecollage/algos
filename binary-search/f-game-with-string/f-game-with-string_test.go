package main

import (
	"testing"
)

// func TestDoesInclude(t *testing.T) {
// 	str1 := "assd"
// 	str2 := "ad"
// 	result := doesInclude(str1, str2)
// 	if !result {
// 		t.Errorf("Result was incorrect, got: %s, want: %s.", result, true)
// 	}

// 	return
// }

// func Test_calculate(t *testing.T) {
// 	type args struct {
// 		t     string
// 		p     string
// 		array []int
// 	}
// 	tests := []struct {
// 		name string
// 		args args
// 		want int
// 	}{
// 		// TODO: Add test cases.
// 	}
// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			if got := calculate(tt.args.t, tt.args.p, tt.args.array); got != tt.want {
// 				t.Errorf("calculate() = %v, want %v", got, tt.want)
// 			}
// 		})
// 	}
// }

func Test_modifySubstring(t *testing.T) {
	type args struct {
		t       string
		exclude []int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "1",
			args: args{
				t:       "ababcba",
				exclude: []int{5, 3},
			},
			want: "ab.b.ba",
		},
		{
			name: "2",
			args: args{
				t:       "ababcba",
				exclude: []int{5},
			},
			want: "abab.ba",
		},
		{
			name: "3",
			args: args{
				t:       "a",
				exclude: []int{1},
			},
			want: ".",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := modifyString(tt.args.t, tt.args.exclude); got != tt.want {
				t.Errorf("modifyString() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_doesInclude(t *testing.T) {
	type args struct {
		searchSubstring string
		origString      string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "1",
			args: args{
				searchSubstring: "abb",
				origString:      "ab.b.ba",
			},
			want: true,
		},
		{
			name: "2",
			args: args{
				searchSubstring: "aba",
				origString:      "ab.b.ba",
			},
			want: true,
		},
		{
			name: "3",
			args: args{
				searchSubstring: "abd",
				origString:      "ab.b.ba",
			},
			want: false,
		},
		{
			name: "4",
			args: args{
				searchSubstring: "a",
				origString:      "ab.b.ba",
			},
			want: true,
		},
		{
			name: "5",
			args: args{
				searchSubstring: "d",
				origString:      "ab.b.ba",
			},
			want: false,
		},
		{
			name: "6",
			args: args{
				searchSubstring: "d",
				origString:      "......",
			},
			want: false,
		},
		{
			name: "7",
			args: args{
				searchSubstring: "abb",
				origString:      "ab...ba",
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := doesInclude(tt.args.searchSubstring, tt.args.origString); got != tt.want {
				t.Errorf("doesInclude() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_calculate(t *testing.T) {
	type args struct {
		t     string
		p     string
		array []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "1",
			args: args{
				t:     "ababcba",
				p:     "abb",
				array: []int{5, 3, 4, 1, 7, 6, 2},
			},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := calculate(tt.args.t, tt.args.p, tt.args.array); got != tt.want {
				t.Errorf("calculate() = %v, want %v", got, tt.want)
			}
		})
	}
}
