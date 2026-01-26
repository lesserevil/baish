/* baish_curl_init.h - Shared curl initialization for baish builtins
 *
 * This header provides thread-unsafe but process-safe curl initialization
 * for bash builtins. Multiple builtins (ask via openai-c, mcp) use libcurl
 * and must coordinate to call curl_global_init() exactly once per process.
 *
 * IMPORTANT: This relies on static variable sharing within the same process.
 * Not thread-safe - assumes single-threaded bash execution.
 */

#ifndef BAISH_CURL_INIT_H
#define BAISH_CURL_INIT_H

#include <curl/curl.h>

/* Shared flag to track if curl has been globally initialized.
 * Defined in baish_curl_init.c to ensure single instance across all builtins.
 */
extern int baish_curl_global_initialized;

/* Initialize curl globally if not already done.
 * Returns 0 on success or if already initialized, -1 on error.
 *
 * Call this once per builtin before first curl usage.
 * Safe to call multiple times - will only init once.
 */
int baish_init_curl_global(void);

/* Cleanup curl global state on shell exit.
 * Currently not called - bash exit handles cleanup implicitly.
 * Included for completeness if bash ever adds builtin cleanup hooks.
 */
void baish_cleanup_curl_global(void);

#endif /* BAISH_CURL_INIT_H */
