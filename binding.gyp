{
  "targets": [
    {
      "target_name": "PyNode",
      "sources": [
        "src/main.cpp",
        "src/helpers.cpp"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ['OS=="win"', {
          "variables": {
            "PY_HOME%": "<!(python -c \"import sysconfig;print(sysconfig.get_paths()['data'])\")"
          },
          "include_dirs": [
            "<!(echo <(PY_HOME)\include)"
          ],
          "msvs_settings": {
            "VCLinkerTool": {
              "AdditionalLibraryDirectories": "<!(echo <(PY_HOME)\libs)"
            }
          }
        }],
        ['OS!="win"', {
          "variables": {
            "PY_INCLUDE%": "<!(if [[ -z $PY_INCLUDE ]]; then echo $(python-config --includes); else echo $PY_INCLUDE; fi)",\
            "PY_LIBS%": "<!(if [[ -z $PY_LIBS ]]; then echo $(python-config --ldflags); else echo $PY_LIBS; fi)"
          },
          "include_dirs": [
            "<(PY_INCLUDE)"
          ],
          "libraries": [
            "<(PY_LIBS)",
          ]
        }]
      ]
    }
  ]
}
