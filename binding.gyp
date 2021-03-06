{
  "targets": [
    {
      "target_name": "addon",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ 
          "<!@(ls -1 src/driver/*.cc)", 
          "<!@(ls -1 librazermacos/src/lib/*.c)" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "librazermacos/src/include"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
            'LDFLAGS': [
          '-framework IOKit',
          '-framework CoreFoundation'
      ],
      'xcode_settings': {
          'VALID_ARCHS': 'arm64e x86_64',
          'ONLY_ACTIVE_ARCH': 'NO',
          'OTHER_CODE_SIGN_FLAGS': 'timestamp --options=runtime',
          'CLANG_CXX_LIBRARY': 'libc++',
          'MACOSX_DEPLOYMENT_TARGET': '11.0',
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          'OTHER_LDFLAGS': [
              '-framework IOKit',
              '-framework CoreFoundation'
          ],
      }
    }
  ]
}
