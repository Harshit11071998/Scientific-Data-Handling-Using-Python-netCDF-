import os
os.environ['PROJ_LIB'] = r'C:\Users\Harshit\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.basemap import Basemap,shiftgrid
from matplotlib import colors as c
#specify the path of you netCDF file
vc_open=nc.Dataset('pv20180416250hpa.nc')

lt=vc_open.variables['latitude'][:]
ln=vc_open.variables['longitude'][:]
a=[float(i) for i in ln]
pv=(vc_open.variables['pv'][:])

time=vc_open.variables['time']
dates = nc.num2date(time[:],units=time.units,calendar=time.calendar)
str_time = [i.strftime("%Y%m%d %H") for i in dates]
csfont = {'fontname':'Arial', 'fontweight' : 'bold', 'fontsize':26, 'color':'black'}
my_color=(['#f5d142','#f5d442','#f5d742','#f5da42','#f5dd42','#f5e042','#f5e342','#f5e642','#f5e942','#f5ec42','#f5ef42',
'#f5f242','#f5f542','#f2f543','#eff542','#ecf542','#e9f542','#e6f542','#e3f542','#e0f542','#ddf542',
'#daf542','#d7f542','#d4f542','#d1f542','#cef542','#cbf542','#c8f542','#c5f542','#c2f542','#bff542',
'#bcf542','#b9f542','#b6f542','#b3f542','#b0f542','#adf542','#aaf542','#a7f542','#a4f542','#a1f542',
'#9ef542','#9cf542','#99f542','#96f542','#93f542','#90f542','#8df542','#8af542','#87f542','#84f542',
'#81f542','#7ef542','#7bf542','#78f542','#75f542','#72f542','#6ff542','#6cf542','#69f542','#66f542',
'#63f542','#60f542','#5df542','#5af542','#57f542','#54f542','#51f542','#4ef542','#4bf542','#48f542',
'#45f542','#42f542','#42f545','#42f548','#42f54b','#42f54e','#42f551','#42f554','#42f557','#42f55a',
'#42f55d','#42f560','#42f563','#42f566','#42f569','#42f56c','#42f56f','#42f572','#42f575','#42f578',
'#42f57b','#42f57e','#42f581','#42f584','#42f587','#42f58a','#42f58d','#42f590','#42f593','#42f596',
'#42f599','#42f59c','#42f59e','#42f5a1','#42f5a4','#42f5a7','#42f5aa','#42f5ad','#42f5b0','#42f5b3',
'#42f5b6','#42f5b9','#42f5b3','#42f5bf','#42f5c2','#42f5c5','#42f5c8','#42f5cb','#42f5ce','#42f5d1',
'#42f5d4','#42f5d7','#42f5da','#42f5dd','#42f5e0','#42f5e3','#42f5e6','#42f5e9','#42f5ec','#42f5ef',
'#42f5f2','#42f5f5','#42f2f5','#42eff5','#42ecf5','#42e9f5','#42e6f5','#42e3f5','#42e0f5','#42ddf5',
'#42daf5','#42d7f5','#42d4f5','#42d1f5','#42cef5','#42cbf5','#42c8f5','#42c5f5','#42c2f5','#43bff5',
'#42bcf5','#42b9f5','#42b6f5','#42b3f5','#42b0f5','#42adf5','#42aaf5','#42a7f5','#42a4f5','#42a1f5',
'#429ef5','#429cf5','#4295f5','#4296f5','#4293f5','#4290f5','#428df5','#428af5','#4287f5','#4284f5',
'#427ef5','#427bf5','#4278f5','#4275f5','#4272f5','#426cf5','#4269f5','#4266f5','#4263f5','#4260f5',
'#425df5','#425af5','#4257f5','#4254f5','#4251f5','#424ef5','#424bf5','#4248f5','#4245f5','#4242f5',
'#4542f5','#4842f5','#4b42f5','#4e42f5','#5142f5','#5442f5','#5742f5','#5a42f5','#5d42f5','#6042f5',
'#6342f5','#6642f5','#6942f5','#6c42f5','#6f42f5','#7242f5','#7542f5','#7842f5','#7b42f5','#7e42f5',
'#8142f5','#8442f5','#8742f5','#8a42f5','#8d42f5','#9042f5','#9342f5','#9642f5','#9942f5','#9c42f5',
'#9e42f5','#a142f5','#a442f5','#a742f5','#aa42f5','#ad42f5','#b042f5','#b342f5','#b642f5','#b942f5',
'#bc42f5','#bf42f5','#c242f5','#c542f5','#c842f5','#cb42f5','#ce42f5','#d142f5','#d442f5','#d742f5',
'#da42f5','#dd42f5','#e042f5','#e342f5','#e642f5','#e942f5','#ec42f5','#ef42f5','#f242f5','#f542f5',
'#f542f2','#f542ef','#f542ec','#f542e9','#f542e6','#f542e3','#f542e0','#f542dd','#f542da','#f542d7',
'#f542d4','#f542d1','#f542ce','#f542cb','#f542c5','#f542c2','#f542bf','#f542bc','#f542b9','#f542b6',
'#f542b3','#f542b0','#f542ad','#f542aa','#f542a7','#f542a4','#f542a1','#f5429e','#f5429c','#f54299',
'#f54296','#f54293','#f54290','#f5428d','#f5428a','#f54287','#f54284','#f54281','#f5427e','#f5427b',
'#f54278','#f54275','#f54272','#f5426f','#f5426c','#f54269','#f54266','#f54263','#f54260','#f5425d',
'#f5425a','#f54257','#f54254','#f54251','#f5424e','#f5424b','#f54248','#f54245','#f54242'
])
#for i in range(1):
print("enter index")
i=int(input())
fig= plt.figure(figsize=(50,50))    
ax = fig.add_subplot(1, 1, 1)  
ax.set_title("%s"%str_time[i],**csfont)
  #2019_07_17_PV700hPa_2019041600
map=Basemap(projection='cyl',llcrnrlat=10,urcrnrlat=70, llcrnrlon=-40 ,urcrnrlon=70,resolution='l', ax=ax)
map.drawcountries(color='black', linewidth=2.5, ax=ax)
map.drawcoastlines(color='k', linewidth=2.5,ax=ax) 
map.drawmapboundary(color='k',linewidth=2.5,ax=ax)
map.drawparallels(np.arange(-90,90, 10),labels=[1,0,0,0],**csfont)
map.drawmeridians(np.arange(-180,180,10),labels=[0,0,0,1],**csfont)
ax.set_ylabel("Latitude ",**csfont,labelpad = 70)
ax.set_xlabel("Longitude",**csfont,labelpad = 40)

pv,lns = shiftgrid(180.,pv,ln,start=False)
llons, llats = np.meshgrid(lns, lt)
x,y=map(llons, llats)
data=(pv[i,:,:])
data=data/0.000001
cmap= c.ListedColormap(my_color)
cmap.set_under('#f5bc42')
bounds=np.linspace(0,10,100,endpoint=True) 
norm = c.BoundaryNorm(bounds, ncolors=cmap.N)
cs=plt.contourf(x,y,data, cmap=cmap,norm=norm,levels=bounds,extend='both',shading='interp')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.2)
cb=fig.colorbar(cs, cmap=cmap,norm=norm, cax=cax, boundaries=bounds,ax=ax, ticks=np.arange(0,11,1), extend='both')
cb.ax.set_yticklabels(np.arange(0,11,1),**csfont)
cb.ax.tick_params(labelsize=26, direction='out', length=8, width=2)
cb.ax.set_ylabel('Potential Vorticity at 250 hPa[PVU]',**csfont,labelpad= 30)
plt.show()