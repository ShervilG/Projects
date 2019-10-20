module traffic_lights(clk,rst,ns,sn,we,ew,nss,sns,wes,ews,nsr,snr,wer,ewr);
    input[1:0] ns,sn,we,ew;
    output[6*8:0] nss,sns,wes,ews,nsr,snr,wer,ewr;
    reg[6*8:0] nss,sns,wes,ews,nsr,snr,wer,ewr;
    input clk,rst; 
    always @(posedge clk)
    begin
        case (ns)
            2'b00 : 
                begin
                    nss = "red";
                    nsr = "red";
                end
            2'b01 : 
                begin
                    nss = "green";
                    nsr = "red";
                end
            2'b10 : 
                begin 
                    nss = "green";
                    nsr = "green";
                end
            default : 
                begin   
                    nss = "red";
                    nsr = "red"; 
                end
        endcase
        case (sn)
            2'b00 : 
                begin
                    sns = "red";
                    snr = "red";
                end
            2'b01 : 
                begin
                    sns = "green";
                    snr = "red";
                end
            2'b10 : 
                begin 
                    sns = "green";
                    snr = "green";
                end
            default : 
                begin   
                    sns = "red";
                    snr = "red"; 
                end
        endcase
        case (we)
            2'b00 : 
                begin
                    wes = "red";
                    wer = "red";
                end
            2'b01 : 
                begin
                    wes = "green";
                    wer = "red";
                end
            2'b10 : 
                begin 
                    wes = "green";
                    wer = "green";
                end
            default : 
                begin   
                    wes = "red";
                    wer = "red"; 
                end
        endcase
        case (ew)
            2'b00 : 
                begin
                    ews = "red";
                    ewr = "red";
                end
            2'b01 : 
                begin
                    ews = "green";
                    ewr = "red";
                end
            2'b10 : 
                begin 
                    ews = "green";
                    ewr = "green";
                end
            default : 
                begin   
                    ews = "red";
                    ewr = "red"; 
                end
        endcase
    end
endmodule

module test;
    reg[1:0] ns;
    reg[1:0] sn;
    reg[1:0] we;
    reg[1:0] ew;
    reg clk,rst;
    wire[6*8:0] nss;
    wire[6*8:0] sns;
    wire[6*8:0] wes;
    wire[6*8:0] ews;
    wire[6*8:0] nsr;
    wire[6*8:0] snr;
    wire[6*8:0] wer;
    wire[6*8:0] ewr;
    integer i;
    //integer i;
    //integer cycles;
    traffic_lights l1(clk,rst,ns,sn,we,ew,nss,sns,wes,ews,nsr,snr,wer,ewr);
    initial
        begin
            $dumpfile("tlc.vcd");
            $dumpvars(0,test);
            $display("nss\t  nsr\t   sns\t   snr\t   wes\t   wer\t   ews\t   ewr\n---------------------------------------------------------------------");
            $monitor("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s",nss,nsr,sns,snr,wes,wer,ews,ewr);
                begin
                    ns = 2'b10;
                end
                #20;
                begin
                    ns = 2'b01;
                    sn = 2'b01;
                end
                #20;
                begin
                    ns = 2'b00;
                    sn = 2'b10;
                end
                #20;
                begin
                    sn = 2'b00;
                    we = 2'b10;
                end
                #20;
                begin
                    we = 2'b01;
                    ew = 2'b01;
                end
                #20;
                begin
                    we = 2'b00;
                    ew = 2'b10;
                end
                #20;
                $finish;
        end
        initial begin
            clk = 0;
            for (i=0;i<=100;i++) 
                #5 clk = ~clk;
            $finish;
        end
endmodule


