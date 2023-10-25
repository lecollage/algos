package main

import (
	"reflect"
	"testing"
)

func Test_calculate(t *testing.T) {
	type args struct {
		n int
		k int
		x int
	}
	tests := []struct {
		name  string
		args  args
		want  bool
		want1 []int
	}{
		// TODO: Add test cases.
		// {
		// 	name:  "1",
		// 	want:  true,
		// 	want1: []int{3, 3, 3, 1},
		// 	args:  args{10, 3, 2},
		// },
		// {
		// 	name:  "2",
		// 	want:  false,
		// 	want1: []int{},
		// 	args:  args{5, 2, 1},
		// },
		// {
		// 	name:  "3",
		// 	want:  true,
		// 	want1: []int{2, 2},
		// 	args:  args{4, 2, 1},
		// },
		// {
		// 	name:  "4",
		// 	want:  false,
		// 	want1: []int{},
		// 	args:  args{6, 1, 1},
		// },
		{
			name:  "5",
			want:  true,
			want1: []int{2, 2, 2},
			args:  args{6, 2, 1},
		},
		{
			name:  "6",
			want:  true,
			want1: []int{4, 1},
			args:  args{5, 4, 3},
		},
		{
			name:  "7",
			want:  false,
			want1: []int{},
			args:  args{1, 1, 1},
		},
		{
			name:  "8",
			want:  false,
			want1: []int{},
			args:  args{0, 1, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := calculate(tt.args.n, tt.args.k, tt.args.x)
			if got != tt.want {
				t.Errorf("calculate() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("calculate() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}
