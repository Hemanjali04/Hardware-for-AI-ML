`timescale 1ns / 1ps

module relu_neuron_tb;

    reg clk, reset;
    reg signed [7:0] input_value;
    wire signed [7:0] output_value;

    relu_neuron uut (
        .clk(clk),
        .reset(reset),
        .input_value(input_value),
        .output_value(output_value)
    );

    initial begin
        clk = 0; forever #5 clk = ~clk;
    end

    initial begin
        $dumpfile("relu_neuron.vcd");
        $dumpvars(0, relu_neuron_tb);

        reset = 1; input_value = 0; #20;
        reset = 0;

        input_value = -10; #10;
        input_value = 5; #10;
        input_value = -3; #10;
        input_value = 12; #10;
        input_value = 0; #10;

        #50;
        $finish;
    end

endmodule