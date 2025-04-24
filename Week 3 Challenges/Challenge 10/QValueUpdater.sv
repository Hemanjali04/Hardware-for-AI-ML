module QValueUpdater (
    input logic clk,
    input logic rst,
    input logic [31:0] current_q,
    input logic [31:0] reward,
    input logic [31:0] max_next_q,
    input logic [31:0] alpha, // Learning rate
    input logic [31:0] gamma, // Discount factor
    output logic [31:0] updated_q
);

    logic [31:0] temp1, temp2, temp3;

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            updated_q <= 32'd0;
        end else begin
            temp1 <= reward + (gamma * max_next_q);     // r + γ * max(Q(s’, a’))
            temp2 <= alpha * temp1;                     // α * (r + γ * maxQ)
            temp3 <= (32'd1 - alpha) * current_q;       // (1 - α) * Q(s, a)
            updated_q <= temp3 + temp2;                 // Final updated Q(s, a)
        end
    end

endmodule