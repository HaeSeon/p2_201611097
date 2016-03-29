import os

mydir=%pwd

mydir
u'C:\\Users\\Kim\\p162'

myplantdir=os.path.join(mydir,'lib')

myplantdir
u'C:\\Users\\Kim\\p162\\lib'

%cd {myplantdir}

mydot='C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe'

import glob

%cd {myplantdir}
C:\Users\Kim\p162\lib

glob.glob(r'./*.jar')
['.\\plantuml.jar']

import os

os.environ['GRAPHVIZ_DOT']=mydot

print os.environ['GRAPHVIZ_DOT']
C:\Program Files (x86)\Graphviz2.38\bin\dot.exe

!java -jar {myplantdir}/plantuml.jar -testdot
The environment variable GRAPHVIZ_DOT has been set to C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
Dot executable is C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
Dot version: dot - graphviz version 2.38.0 (20140413.2041)

Installation seems OK. File generation OK


%install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py
Installed plantuml_magics.py. To use it, type:
  %load_ext plantuml_magics

%load_ext plantuml_magics
The plantuml_magics extension is already loaded. To reload it, use:
  %reload_ext plantuml_magics



%%plantuml
@startuml
start

:fd 100;
:right 90;
:fd 100;
:right 90;
:fd 100;
:right 90;
:fd 100;
:right 90;
stop
@enduml