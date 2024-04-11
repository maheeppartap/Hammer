# Hammer - Fault Localization and Automatic Program repair

Welcome!

This is an under-construction repo of a much larger Automatic Program Repair tool. This is not yet fully ready, but some aspects of this work very well!

For now, only the fault localization is working. Given some C++ code, and some tests, this will find the buggy lines for you. I have implemented 12 different types of fault localizations using Similarity coefficient based techniques:
  - Kulczynski
  - Simple-Matching
  - BraunBanquet
  - Dennis
  - Mountford
  - Fossum
  - Pearson
  - Gower
  - Michael
  - Pierce
  - Baroni-Urbani/Buser
  - Tarwid
  - D*

out of all these D* is the best performing ones. If you're reading this now, you are more than welcome to use any of these, but keep in mind, this is always evolving!

The next step is to implement a good code mutation tool that can alter the source code to find something that passes the given constriants, and/or satisfies some heuristic. 
