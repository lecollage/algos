// package main

// import "testing"

// func Test_binSearch(t *testing.T) {
// 	type args struct {
// 		array       []int
// 		searchValue int
// 	}
// 	tests := []struct {
// 		name string
// 		args args
// 		want int
// 	}{
// 		{name: '1',
// 			args: {
// 				array:       []int{1, 2, 3, 3, 3, 3, 4, 5},
// 				searchValue: 3,
// 			},
// 			want: 2,
// 		},
// 	}
// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			if got := binSearch(tt.args.array, tt.args.searchValue); got != tt.want {
// 				t.Errorf("binSearch() = %v, want %v", got, tt.want)
// 			}
// 		})
// 	}
// }
