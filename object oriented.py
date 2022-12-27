class INT108:
      coursename="python programming"
      def __init__(self,session,year,batchname,blockno):
           self.session=session
           self.year=year
           self.batchname=batchname
           self.blockno=blockno
      def info(self):
           print("this is {} batch".format(self.batchname))
koc39=INT108("july-dec",2022,"koc39",34)
koc39.info()
