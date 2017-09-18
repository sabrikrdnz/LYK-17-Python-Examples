import os
os.mkdir("/Users/ghost/Desktop/osdeneme") # dizin oluşturma
os.rmdir("/Users/ghost/Desktop/osdeneme") # içi boşsa dizin silme
os.remove("/Users/ghost/Desktop/osdeneme") # içi boş değilse
os.uname() #os bilgilerini tuple olarak döner.
os.uname().machine # mimariyi döner
os.uname().nodename #bilgisayarın adını döner

