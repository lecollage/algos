package main

import (
	"reflect"
	"testing"
)

func Test_calculate(t *testing.T) {
	type args struct {
		workers      []Worker
		baloonsCount int
	}
	tests := []struct {
		name  string
		args  args
		want  int
		want1 []Worker
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := calculate(tt.args.workers, tt.args.baloonsCount)
			if got != tt.want {
				t.Errorf("calculate() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("calculate() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_canProduceBaloons(t *testing.T) {
	type args struct {
		availableTime int
		workers       []Worker
		baloonsCount  int
	}
	tests := []struct {
		name  string
		args  args
		want  bool
		want1 []Worker
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := canProduceBaloons(tt.args.availableTime, tt.args.workers, tt.args.baloonsCount)
			if got != tt.want {
				t.Errorf("canProduceBaloons() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("canProduceBaloons() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_howManyBaloonsMayProduce(t *testing.T) {
	type args struct {
		availableTime int
		worker        Worker
	}
	tests := []struct {
		name string
		args args
		want int
	}{{
		name: "0",
		want: 0,
		args: args{
			availableTime: 1,
			worker: Worker{
				t: 2, z: 1, y: 1, work: 0, id: 0,
			},
		},
	}, {
		name: "1",
		want: 1,
		args: args{
			availableTime: 1,
			worker: Worker{
				t: 1, z: 1, y: 1, work: 0, id: 0,
			},
		},
	}, {
		name: "2",
		want: 1,
		args: args{
			availableTime: 2,
			worker: Worker{
				t: 2, z: 1, y: 1, work: 0, id: 0,
			},
		},
	}, {
		name: "3",
		want: 3,
		args: args{
			availableTime: 8,
			worker: Worker{
				t: 2, z: 1, y: 1, work: 0, id: 0,
			},
		},
	}, {
		name: "4",
		want: 3,
		args: args{
			availableTime: 7,
			worker: Worker{
				t: 2, z: 2, y: 1, work: 0, id: 0,
			},
		},
	}, {
		name: "5",
		want: 2,
		args: args{
			availableTime: 7,
			worker: Worker{
				t: 3, z: 2, y: 2, work: 0, id: 0, // 3 + 3
			},
		},
	}, {
		name: "6",
		want: 5,
		args: args{
			availableTime: 20,
			worker: Worker{
				t: 3, z: 2, y: 2, work: 0, id: 0, // 3 + 3 + 2 + 3 + 3 + 2 + 3 + 3 + 2
			},
		},
	}}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := howManyBaloonsMayProduce(tt.args.availableTime, tt.args.worker); got != tt.want {
				t.Errorf("howManyBaloonsMayProduce() = %v, want %v", got, tt.want)
			}
		})
	}
}
