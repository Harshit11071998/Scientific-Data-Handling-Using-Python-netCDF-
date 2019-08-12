import os
os.environ['PROJ_LIB'] = r'C:\Users\Harshit\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap,shiftgrid
from mpl_toolkits.axes_grid1 import make_axes_locatable

vc_open=nc.Dataset('MSLP20190422.nc')
lt=vc_open.variables['latitude'][:]
ln=vc_open.variables['longitude'][:]
mslp=(vc_open.variables['msl'][:])
mslp = mslp*0.01
time=vc_open.variables['time']
dates = nc.num2date(time[:],units=time.units,calendar=time.calendar)
str_time = [i.strftime("%Y%m%d %H") for i in dates]

vc1_open =nc.Dataset('UVWIND20190422925hpa.nc')
uwnd = vc1_open.variables['u'][:]
vwnd = vc1_open.variables['v'][:]

lon1=-40
lon2=70
lat1=10
lat2=70

llat=20
ulat=50
llon=-20
rlon=20 

csfont = {'fontname':'Arial', 'fontweight' : 'bold', 'fontsize':26, 'color':'black'}
print("Enter the Index for Time")
i = int(input())
fig= plt.figure(figsize=(50,50))    
ax = fig.add_subplot(1, 1, 1)  
ax.set_title("%s"%str_time[i],**csfont)
  
map=Basemap(projection='cyl',llcrnrlat=lat1,urcrnrlat=lat2, llcrnrlon=lon1,urcrnrlon=lon2,resolution='l', ax=ax)
map.drawcountries(color='black', linewidth=2.5, ax=ax)
map.drawcoastlines(color='k', linewidth=2.5,ax=ax) 
map.drawmapboundary(color='k',linewidth=2.5,ax=ax)
map.drawparallels(np.arange(-90,90, 10),labels=[1,0,0,0],**csfont)
map.drawmeridians(np.arange(-180,180,10),labels=[0,0,0,1],**csfont)
ax.set_ylabel("Latitude ",**csfont,labelpad = 70)
ax.set_xlabel("Longitude",**csfont,labelpad = 40)

mslp, lns = shiftgrid(180.,mslp,ln,start=False)
uwnd,lns = shiftgrid(180.,uwnd,ln,start=False)
vwnd,lns = shiftgrid(180.,vwnd,ln,start=False)
  
llons, llats =np.meshgrid(lns,lt)
x,y =map(llons, llats)
data=(mslp[i,:,:])
uwnd =(uwnd[i,:,:])
vwnd =(vwnd[i,:,:])
   
bounds=np.linspace(1000,1030,1000,endpoint=True)         

cs=plt.contourf(x,y,data, cmap="RdYlBu_r", shading='interp', levels=bounds,extend='both')
map.streamplot(x, y, uwnd,vwnd, color='k', density = 10., linewidth=2.5, arrowsize=2.5, arrowstyle='->', minlength=0.1, maxlength=5.0)
  
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.2)
cb=fig.colorbar(cs, cmap="RdYlBu_r", cax=cax, boundaries=bounds,ax=ax, ticks=np.arange(1000,1031,5), extend='both')
cb.ax.set_yticklabels(np.arange(1000,1031,5),**csfont)
cb.ax.tick_params(labelsize=26, direction='out', length=8, width=2)
cb.ax.set_ylabel('Mean Sea Level Pressure (hPa)',**csfont,labelpad= 30)

plt.show()