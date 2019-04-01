- This is ONLY for Windows
- Ingredients
  - R 3.4.x and Rstudio
  - R 3.5.x doesn't work with rClr_0.7-4 binary at this moment
  - Download ROSIsoft.zip from https://pisquare.osisoft.com/blogs/holgeramort/2018/02/19/rosisoft-osisoft-pi-and-r-version-2
  - OSIsoft.AFSDK.dll must exist in C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0

- Installing ROSIsoft.zip
  - Download the file from https://pisquare.osisoft.com/blogs/holgeramort/2018/02/19/rosisoft-osisoft-pi-and-r-version-2
    - Extract rClr_0.7-4.zip
  - Tools -> Install Packages -> Install from: Package Archive File
    - Install rClr_0.7-4.zip and ROSIsoft.zip

- Sample run
  - In R CLI
    - library(ROSIsoft)
    - AFSetup()
    - con <- ConnectToPIWithPrompt('cmssvm166')
      - Will ask username/password
    - con$IsPIConnected
      - TRUE or FALSE
    - data <- GetPointValues('SINUSOID', '2018-Dec-11 01:45:00', '2018-Dec-12 05:55:00', 'interpolated',10)
    - head(data)
    - FindPointsbyName('*sinu*')
      - Find PI tags which have 'sinu' in the name
    - data <- GetPointValues('SINUSOID', '2018-Oct-13 03:15:00', '2018-Oct-14 03:25:00', 'recorded',1)
      - Pull data as recorded
      - "1" in the end is a dummy

