module lif_neuron_array #(parameter N = 4)(
    input wire clk,
    input wire reset,
    input wire [N-1:0] spike_in,
    output wire [N-1:0] spike_out
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : neuron_gen
            lif_neuron neuron_inst (
                .clk(clk),
                .reset(reset),
                .spike_in(spike_in[i]),
                .spike_out(spike_out[i])
            );
        end
    endgenerate
endmodule