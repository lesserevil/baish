/* baish_curl_init.c - Shared curl initialization implementation
 *
 * This file provides the single global instance of curl initialization state
 * shared across all baish builtins that use libcurl (ask/openai-c, mcp).
 */

#include <config.h>
#include "baish_curl_init.h"

/* Global flag - single instance shared across all builtins in the process */
int baish_curl_global_initialized = 0;

int
baish_init_curl_global(void)
{
  if (baish_curl_global_initialized)
    return 0;

  if (curl_global_init(CURL_GLOBAL_DEFAULT) != 0)
    return -1;

  baish_curl_global_initialized = 1;
  return 0;
}

void
baish_cleanup_curl_global(void)
{
  if (baish_curl_global_initialized) {
    curl_global_cleanup();
    baish_curl_global_initialized = 0;
  }
}
