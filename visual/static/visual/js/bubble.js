var w = window.innerWidth*0.68*0.95;
   var h = Math.ceil(w*0.7);
   var oR = 0;
   var nTop = 0;
    
   var svgContainer = d3.select("#mainBubble")
      .style("height", h+"px");
    
   var svg = d3.select("#mainBubble").append("svg")
        .attr("class", "mainBubbleSVG")
        .attr("width", w)
        .attr("height",h)
        .on("mouseleave", function() {return resetBubbles();});

 
    d3.json("/static/visual/js/main_bubble.json", function(error, root) {
        console.log(error);
     
        var bubbleObj = svg.selectAll(".topBubble")
                .data(root.children)
            	.enter().append("g")
                .attr("id", function(d,i) {return "topBubbleAndText_" + i;});
             
        console.log(root);  
        nTop = root.children.length;
        oR = w/(1+3*nTop);  
 
    h = Math.ceil(w/nTop*2);
    svgContainer.style("height",h+"px");
         
        var colVals = d3.scale.category10().range(['#777', '#000', '#b3b3b3', '#444']);
         
        bubbleObj.append("circle")
            .attr("class", "topBubble")
            .attr("id", function(d,i) {return "topBubble" + i;})
            .attr("r", function(d) { return oR; })
            .attr("cx", function(d, i) {return oR*(3*(1+i)-1);})
            .attr("cy", (h+oR)/3)
            .style("fill", function(d,i) { return colVals(i); }) // #1f77b4
        	.style("opacity",0.2)
            .on("mouseover", function(d,i) {return activateBubble(d,i);});
         
             
        bubbleObj.append("text")
            .attr("class", "topBubbleText")
            .attr("x", function(d, i) {return oR*(3*(1+i)-1);})
            .attr("y", (h+oR)/3)
        .style("fill", function(d,i) { return colVals(i); }) // #1f77b4
            .attr("font-size", 12)
            .attr("text-anchor", "middle")
        .attr("dominant-baseline", "middle")
        .attr("alignment-baseline", "middle")
            .text(function(d) {return d.name;})      
            .on("mouseover", function(d,i) {return activateBubble(d,i);});
         
        }); 
 
    resetBubbles = function () {
      w = window.innerWidth*0.68*0.95;
      oR = w/(1+3*nTop);
       
      h = Math.ceil(w/nTop*2);
      svgContainer.style("height",h+"px");
 
           
      svg.attr("width", w);
      svg.attr("height",h);       
       
       
      var t = svg.transition()
          .duration(650);
         
        t.selectAll(".topBubble")
            .attr("r", function(d) { return oR; })
            .attr("cx", function(d, i) {return oR*(3*(1+i)-1);})
            .attr("cy", (h+oR)/3);
 
        t.selectAll(".topBubbleText")
            .text(function(d) {return d.name;})      
        	.attr("font-size", 12)
            .attr("x", function(d, i) {return oR*(3*(1+i)-1);})
            .attr("y", (h+oR)/3);
     
    };
         
         
        function activateBubble(d,i) {
            // increase this bubble and decrease others
            var t = svg.transition()
                .duration(d3.event.altKey ? 7500 : 350);
     
            t.selectAll(".topBubble")
                .attr("cx", function(d,ii){
                    if(i == ii) {
                        // Nothing to change
                        return oR*(3*(1+ii)-1) - 0.6*oR*(ii-1);
                    } else {
                        // Push away a little bit
                        if(ii < i){
                            // left side
                            return oR*0.6*(3*(1+ii)-1);
                        } else {
                            // right side
                            return oR*(nTop*3+1) - oR*0.6*(3*(nTop-ii)-1);
                        }
                    }               
                })
                .attr("r", function(d, ii) { 
                    if(i == ii)
                        return oR*1.8;
                    else
                        return oR*0.8;
                    });
                     
            t.selectAll(".topBubbleText")
            	.text(function(d, ii){
            		if (i ==ii )
            			return (d.description + ": " + d.value);
            		else
            			return d.name;
            		})
                .attr("x", function(d,ii){
                    if(i == ii) {
                        // Nothing to change
                        return oR*(3*(1+ii)-1) - 0.6*oR*(ii-1);
                    } else {
                        // Push away a little bit
                        if(ii < i){
                            // left side
                            return oR*0.6*(3*(1+ii)-1);
                        } else {
                            // right side
                            return oR*(nTop*3+1) - oR*0.6*(3*(nTop-ii)-1);
                        }
                    }               
                })          
                .attr("font-size", function(d,ii){
                    if(i == ii)
                        return 12*1.5;
                    else
                        return 12*0.6;              
                });
              
        }
     
    window.onresize = resetBubbles;