module INV_X1(.I(in), .ZN(out));
input in;
output out;
assign out = ~in;
endmodule

module INV_X2(.I(in), .ZN(out));
input in;
output out;
assign out = ~in;
endmodule

module INV_X12(.I(in), .ZN(out));
input in;
output out;
assign out = ~in;
endmodule

module INV_X4(.I(in), .ZN(out));
input in;
output out;
assign out = ~in;
endmodule

module INV_X8(.I(in), .ZN(out));
input in;
output out;
assign out = ~in;
endmodule

module NAND2_X1(.A1(a), .A2(b), .ZN(out));
input a, b;
output out;
assign out = ~(a & b);
endmodule

module NAND2_X2(.A1(a), .A2(b), .ZN(out));
input a, b;
output out;
assign out = ~(a & b);
endmodule

module AND2_X1(.A1(a), .A2(b), .Z(out));
input a, b;
output out;
assign out = (a & b);
endmodule

module AND2_X2(.A1(a), .A2(b), .Z(out));
input a, b;
output out;
assign out = (a & b);
endmodule


module NOR2_X1(.A1(a), .A2(b), .ZN(out));
input a, b;
output out;
assign out = ~(a | b);
endmodule

module NOR2_X2(.A1(a), .A2(b), .ZN(out));
input a, b;
output out;
assign out = ~(a | b);
endmodule

module OR2_X1(.A1(a), .A2(b), .Z(out));
input a, b;
output out;
assign out = (a | b);
endmodule

module OR2_X2(.A1(a), .A2(b), .Z(out));
input a, b;
output out;
assign out = (a | b);
endmodule


module XOR2_X1(.A1(a), .A2(b), .Z(out));
input a, b;
output out;
assign out = (a ^ b);
endmodule

module XNOR2_X1(.A1(a), .A2(b), .ZN(out));
input a, b;
output out;
assign out = ~(a ^ b);
endmodule

module DFFRNQ_X1(.D(d), .CLK(clk), .RN(rnot), .Q(q));
input d, clk, rnot;
output q;
reg q;
always @(posedge clk or negedge rnot)
  if (rnot == 1'b0)
    q = 1'b0;
  else
    q = d;
endmodule

module DFFSNQ_X1( .D(d), .CLK(clk), .SN(snot), .Q(q));
input d, clk, snot;
output q;
reg q;
always @(posedge clk or negedge snot)
  if (snot == 1'b1)
    q = 1'b0;
  else
    q = d;
endmodule

module BUF_X1(.I(in), .Z(out));
input in;
output out;
assign out=in;
endmodule

module BUF_X2(.I(in), .Z(out));
input in;
output out;
assign out=in;
endmodule

module BUF_X4(.I(in), .Z(out));
input in;
output out;
assign out=in;
endmodule

module BUF_X8(.I(in), .Z(out));
input in;
output out;
assign out=in;
endmodule