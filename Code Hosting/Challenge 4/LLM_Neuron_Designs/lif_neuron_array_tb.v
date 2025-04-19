`timescale 1ns / 1ps

module lif_neuron_array_tb;

    reg clk, reset;
    reg [3:0] spike_in;
    wire [3:0] spike_out;

    lif_neuron_array uut (
        .clk(clk),
        .reset(reset),
        .spike_in(spike_in),
        .spike_out(spike_out)
    );

    initial begin
        clk = 0; forever #5 clk = ~clk;
    end

    initial begin
        $dumpfile("lif_neuron_array.vcd");
        $dumpvars(0, lif_neuron_array_tb);

        reset = 1; spike_in = 0; #20;
        reset = 0;

        repeat(4) begin
            spike_in = 4'b0101; #10;
            spike_in = 4'b0000; #10;
        end

        #50;
        $finish;
    end
endmodule