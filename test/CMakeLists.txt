CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
SET(fw_test "${fw_name}-test")

INCLUDE_DIRECTORIES(../include)
link_directories(${CMAKE_SOURCE_DIR}/../)

INCLUDE(FindPkgConfig)
pkg_check_modules(${fw_test} REQUIRED mm-player appcore-efl elementary ecore evas ecore-x capi-media-sound-manager)
FOREACH(flag ${${fw_test}_CFLAGS})
    SET(EXTRA_CFLAGS "${EXTRA_CFLAGS} ${flag}")
ENDFOREACH(flag)

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${EXTRA_CFLAGS} -Wall -Werror")

aux_source_directory(. sources)
FOREACH(src ${sources})
    GET_FILENAME_COMPONENT(src_name ${src} NAME_WE)
    MESSAGE("${src_name}")
    ADD_EXECUTABLE(${src_name} ${src})
    TARGET_LINK_LIBRARIES(${src_name} capi-media-player ${${fw_test}_LDFLAGS})
ENDFOREACH()

