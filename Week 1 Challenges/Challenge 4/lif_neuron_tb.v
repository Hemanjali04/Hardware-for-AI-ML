`timescale 1ns / 1ps

module lif_neuron_tb;

    reg clk, reset, spike_in;
    wire spike_out;

    lif_neuron uut (
        .clk(clk),
        .reset(reset),
        .spike_in(spike_in),
        .spike_out(spike_out)
    );

    initial begin
        clk = 0; forever #5 clk = ~clk;
    end

    initial begin
        $dumpfile("lif_neuron.vcd");
        $dumpvars(0, lif_neuron_tb);

        reset = 1; spike_in = 0; #20;
        reset = 0;

        spike_in = 1; #10;
        spike_in = 0; #10;
        spike_in = 1; #10;
        spike_in = 0; #10;
        spike_in = 1; #10;
        spike_in = 0; #10;
        spike_in = 1; #10;
        spike_in = 0; #50;

        $finish;
    end
endmodule