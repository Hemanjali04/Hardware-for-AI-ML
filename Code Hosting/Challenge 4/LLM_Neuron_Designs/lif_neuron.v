module lif_neuron (
    input wire clk,
    input wire reset,
    input wire spike_in,
    output reg spike_out
);
    parameter THRESHOLD = 8;
    parameter LEAK = 1;
    reg [7:0] membrane_potential;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            membrane_potential <= 0;
            spike_out <= 0;
        end else begin
            if (spike_in) membrane_potential <= membrane_potential + 2;
            if (membrane_potential > LEAK)
                membrane_potential <= membrane_potential - LEAK;
            else
                membrane_potential <= 0;

            if (membrane_potential >= THRESHOLD) begin
                spike_out <= 1;
                membrane_potential <= 0;
            end else begin
                spike_out <= 0;
            end
        end
    end
endmodule