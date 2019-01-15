import time

from ..version import __version__
from . import oer
from . import uper
from .utils import camel_to_snake_case


HEADER_FMT = '''\
/**
 * The MIT License (MIT)
 *
 * Copyright (c) 2018-2019 Erik Moqvist
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use, copy,
 * modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/**
 * This file was generated by asn1tools version {version} {date}.
 */

#ifndef {include_guard}
#define {include_guard}

#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>

#ifndef ENOMEM
#    define ENOMEM 12
#endif

#ifndef EINVAL
#    define EINVAL 22
#endif

#ifndef EOUTOFDATA
#    define EOUTOFDATA 500
#endif

#ifndef EBADCHOICE
#    define EBADCHOICE 501
#endif

#ifndef EBADLENGTH
#    define EBADLENGTH 502
#endif

{structs}
{declarations}
#endif
'''

SOURCE_FMT = '''\
/**
 * The MIT License (MIT)
 *
 * Copyright (c) 2018-2019 Erik Moqvist
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use, copy,
 * modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/**
 * This file was generated by asn1tools version {version} {date}.
 */

#include <string.h>

#include "{header}"

{helpers}
{definitions}\
'''

FUZZER_SOURCE_FMT = '''\
/**
 * The MIT License (MIT)
 *
 * Copyright (c) 2018-2019 Erik Moqvist
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use, copy,
 * modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/**
 * This file was generated by asn1tools version {version} {date}.
 */

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

#include "{header}"

static void assert_first_encode(ssize_t res)
{{
    if (res < 0) {{
        printf("First encode failed with %ld.\\n", res);
        __builtin_trap();
    }}
}}

static void assert_second_decode(ssize_t res)
{{
    if (res < 0) {{
        printf("Second decode failed with %ld.\\n", res);
        __builtin_trap();
    }}
}}

static void assert_second_decode_data(const void *decoded_p,
                                      const void *decoded2_p,
                                      size_t size)
{{
    if (memcmp(decoded_p, decoded2_p, size) != 0) {{
        printf("Second decode data does not match first decoded data.\\n");
        __builtin_trap();
    }}
}}

static void assert_second_encode(ssize_t res, ssize_t res2)
{{
    if (res != res2) {{
        printf("Second encode result %ld does not match first pack "
               "result %ld.\\n",
               res,
               res2);
        __builtin_trap();
    }}
}}

static void assert_second_encode_data(const uint8_t *encoded_p,
                                      const uint8_t *encoded2_p,
                                      ssize_t size)
{{
    ssize_t i;

    if (memcmp(encoded_p, encoded2_p, size) != 0) {{
        for (i = 0; i < size; i++) {{
            printf("[%04ld]: 0x%02x 0x%02x\\n", i, encoded_p[i], encoded2_p[i]);
        }}

        __builtin_trap();
    }}
}}

{tests}

int LLVMFuzzerTestOneInput(const uint8_t *data_p, size_t size)
{{
{llvm_body}

    return (0);
}}
'''

FUZZER_MAKEFILE_FMT = '''\
#
# The MIT License (MIT)
#
# Copyright (c) 2018-2019 Erik Moqvist
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#
# This file was generated by asn1tools version {version} {date}.
#

CC = clang
EXE = fuzzer
C_SOURCES = \\
\t{source} \\
\t{fuzzer_source}
CFLAGS = \\
\t-fprofile-instr-generate \\
\t-fcoverage-mapping \\
\t-I. \\
\t-g -fsanitize=address,fuzzer \\
\t-fsanitize=signed-integer-overflow \\
\t-fno-sanitize-recover=all
EXECUTION_TIME ?= 5

all:
\t$(CC) $(CFLAGS) $(C_SOURCES) -o $(EXE)
\trm -f $(EXE).profraw
\tLLVM_PROFILE_FILE="$(EXE).profraw" \\
\t    ./$(EXE) \\
\t    -max_total_time=$(EXECUTION_TIME)
\tllvm-profdata merge -sparse $(EXE).profraw -o $(EXE).profdata
\tllvm-cov show ./$(EXE) -instr-profile=$(EXE).profdata
\tllvm-cov report ./$(EXE) -instr-profile=$(EXE).profdata

'''

TEST_FMT = '''
static void test_{name}(
    const uint8_t *encoded_p,
    size_t size)
{{
    ssize_t res;
    ssize_t res2;
    ssize_t i;
    uint8_t encoded[size];
    uint8_t encoded2[size];
    struct {name}_t decoded;
    struct {name}_t decoded2;

    memset(&decoded, 0, sizeof(decoded));

    res = {name}_decode(
        &decoded,
        encoded_p,
        size);

    if (res >= 0) {{
        res = {name}_encode(
            &encoded[0],
            sizeof(encoded),
            &decoded);

        assert_first_encode(res);

        memset(&decoded2, 0, sizeof(decoded2));

        res2 = {name}_decode(
            &decoded2,
            &encoded[0],
            res);

        assert_second_decode(res2);
        assert_second_decode_data(&decoded,
                                  &decoded2,
                                  sizeof(decoded));

        res2 = {name}_encode(
            &encoded2[0],
            sizeof(encoded2),
            &decoded);

        assert_second_encode(res, res2);
        assert_second_encode_data(&encoded[0], &encoded2[0], res);
    }}
}}\
'''


def _generate_fuzzer_source(namespace,
                            compiled,
                            date,
                            header_name,
                            source_name,
                            fuzzer_source_name):
    tests = []
    calls = []

    for module_name, module in sorted(compiled.modules.items()):
        for type_name in sorted(module):
            name = '{}_{}_{}'.format(namespace,
                                     camel_to_snake_case(module_name),
                                     camel_to_snake_case(type_name))

            test = TEST_FMT.format(name=name)
            tests.append(test)

            call = '    test_{}(data_p, size);'.format(name)
            calls.append(call)

    source = FUZZER_SOURCE_FMT.format(version=__version__,
                                      date=date,
                                      header=header_name,
                                      tests='\n'.join(tests),
                                      llvm_body='\n'.join(calls))

    makefile = FUZZER_MAKEFILE_FMT.format(version=__version__,
                                          date=date,
                                          source=source_name,
                                          fuzzer_source=fuzzer_source_name)

    return source, makefile


def generate(compiled,
             codec,
             namespace,
             header_name,
             source_name,
             fuzzer_source_name):
    """Generate C source code from given compiled specification.

    `namespace` is used as a prefix for all defines, data structures
    and functions.

    `header_name` is the file name of the C header file, which is
    included by the C source file.

    `source_name` is the file name of the C source file, which is
    needed by the fuzzer makefile.

    `fuzzer_source_name` is the file name of the C source file, which
    is needed by the fuzzer makefile.

    This function returns a tuple of the C header and source files as
    strings.

    """

    date = time.ctime()
    namespace = camel_to_snake_case(namespace)
    include_guard = '{}_H'.format(namespace.upper())

    if codec == 'oer':
        structs, declarations, helpers, definitions = oer.generate(
            compiled,
            namespace)
    elif codec == 'uper':
        structs, declarations, helpers, definitions = uper.generate(
            compiled,
            namespace)
    else:
        raise Exception()

    header = HEADER_FMT.format(version=__version__,
                               date=date,
                               include_guard=include_guard,
                               structs=structs,
                               declarations=declarations)

    source = SOURCE_FMT.format(version=__version__,
                               date=date,
                               header=header_name,
                               helpers=helpers,
                               definitions=definitions)

    fuzzer_source, fuzzer_makefile = _generate_fuzzer_source(
        namespace,
        compiled,
        date,
        header_name,
        source_name,
        fuzzer_source_name)

    return header, source, fuzzer_source, fuzzer_makefile
