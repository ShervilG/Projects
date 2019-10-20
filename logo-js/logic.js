var cv = document.getElementById('lc');
var ctx = cv.getContext("2d");
var w = cv.width;
var h = cv.height;

var t1 = document.getElementById('t1');
var t2 = document.getElementById('t2');

class turtle {
    constructor() {
        this.x = w/2;
        this.y = h/2;
        this.rad = 5;
        this.direction = "up";
    }
    make_turtle(x,y) 
    {
        this.x = x;
        this.y = y;
        ctx.beginPath();
        ctx.fillStyle = "white";
        ctx.arc(x,y,this.rad,0,(Math.PI)*2,false);
        ctx.fill();
        ctx.closePath();
    }
    move_turtle(dist) {
        if (this.direction == "up") {
            ctx.beginPath();
            ctx.fillStyle = "black";
            ctx.strokeStyle = "black";
            ctx.arc(this.x,this.y,this.rad,0,(Math.PI)*2,false);
            ctx.fill();
            ctx.stroke();
            ctx.closePath();
            ctx.beginPath();
            ctx.moveTo(this.x,this.y);
            ctx.fillStyle = "white";
            ctx.strokeStyle = "white";
            this.y = this.y - dist;
            ctx.lineTo(this.x,this.y);
            ctx.stroke();
            ctx.closePath();
            this.make_turtle(this.x,this.y);
            this.direction = "up";
            this.x = this.x;
            this.y = this.y;
            this.direction = "up";
        }
        else if(this.direction == "left") {
            ctx.beginPath();
            ctx.fillStyle = "black";
            ctx.strokeStyle = "black";
            ctx.arc(this.x,this.y,this.rad,0,(Math.PI)*2,false);
            ctx.fill();
            ctx.stroke();
            ctx.closePath();
            ctx.beginPath();
            ctx.moveTo(this.x,this.y);
            ctx.fillStyle = "white";
            ctx.strokeStyle = "white";
            this.x = this.x - dist;
            ctx.lineTo(this.x,this.y);
            ctx.stroke();
            ctx.closePath();
            this.make_turtle(this.x,this.y);
            this.direction = "left";
        }
        else if(this.direction == "down") {
            ctx.beginPath();
            ctx.fillStyle = "black";
            ctx.strokeStyle = "black";
            ctx.arc(this.x,this.y,this.rad,0,(Math.PI)*2,false);
            ctx.fill();
            ctx.stroke();
            ctx.closePath();
            ctx.beginPath();
            ctx.moveTo(this.x,this.y);
            ctx.fillStyle = "white";
            ctx.strokeStyle = "white";
            this.y = this.y + dist;
            ctx.lineTo(this.x,this.y);
            ctx.stroke();
            ctx.closePath();
            this.make_turtle(this.x,this.y);
            this.direction = "down";
        }
        else if(this.direction == "right") {
            ctx.beginPath();
            ctx.fillStyle = "black";
            ctx.strokeStyle = "black";
            ctx.arc(this.x,this.y,this.rad,0,(Math.PI)*2,false);
            ctx.fill();
            ctx.stroke();
            ctx.closePath();
            ctx.beginPath();
            ctx.moveTo(this.x,this.y);
            ctx.fillStyle = "white";
            ctx.strokeStyle = "white";
            this.x = this.x + dist;
            ctx.lineTo(this.x,this.y);
            ctx.stroke();
            ctx.closePath();
            this.make_turtle(this.x,this.y);
            this.direction = "right";
        }
    }
}

var slow_boi = new turtle();
slow_boi.direction = "up";
slow_boi.make_turtle(w/2,h/2);

function take_command(turt) {
    var text = t1.value;
    if (text.search("fd") != -1) {
        var ind = text.indexOf("fd");
        var p = text[ind+3];
        for(var i = ind+4;i<text.length;i++) {
            p = p+text[i];
        }
        turt.move_turtle(parseInt(p, 10));    
    }
     if (text.search("rt") != -1) {
        var ind = text.indexOf("rt");
        var p = text[ind+3];
        for(var i = ind+4;i<text.length;i++) {
            p = p+text[i];
        }
        if (p=="90") {
            if (slow_boi.direction == "up")
                slow_boi.direction = "right";
            else if (slow_boi.direction == "left")
                slow_boi.direction = "up";
            else if (slow_boi.direction == "right")
                slow_boi.direction = "down";
            else if (slow_boi.direction == "down")
                slow_boi.direction = "left";
        }
    }
    t2.value = slow_boi.direction;
}

