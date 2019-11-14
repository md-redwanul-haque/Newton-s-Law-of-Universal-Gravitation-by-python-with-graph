from pylab import plot,show,legend,title,xlabel,ylabel,savefig,legend



def create_graph(x,y):
    plot(x,y,marker='o')
    xlabel('Distance in meter ')
    ylabel('grivitional Force')
    title('gravitional force ')
    legend([100, 1001, 50])
    
    
    
def generate_F_r():
    r = range(100,1001,50)
    F=[]
    G= 6.674*(10**-11)
    m1=0.5
    m2=1.5
    savefig('graph.png')
    
    for dist in r:
        force=G*(m1*m2)/(dist**2)
        F.append(force)
    create_graph(r,F)

if __name__ == '__main__':
    generate_F_r()
    
    

        
    
        
        
    
