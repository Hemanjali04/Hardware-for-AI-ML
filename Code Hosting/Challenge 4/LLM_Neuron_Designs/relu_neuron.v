module relu_neuron (
    input wire clk,
    input wire reset,
    input wire signed [7:0] input_value,
    output reg signed [7:0] output_value
);

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            output_value <= 0;
        end else begin
            if (input_value > 0)
                output_value <= input_value;
            else
                output_value <= 0;
        end
    end

endmodule