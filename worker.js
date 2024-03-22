// For Fixing CORS issue
// CORS Fix Start

const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, HEAD, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
};

function handleOptions(request) {
    if (
        request.headers.get("Origin") !== null &&
        request.headers.get("Access-Control-Request-Method") !== null &&
        request.headers.get("Access-Control-Request-Headers") !== null
    ) {
        return new Response(null, {
            headers: corsHeaders,
        });
    } else {
        return new Response(null, {
            headers: {
                Allow: "GET, HEAD, POST, OPTIONS",
            },
        });
    }
}

// CORS Fix End

import { IncreasePageViews } from "./dbHandler.js";

export default {
    async fetch(request, env, ctx) {
        if (request.method === "OPTIONS") {
            // Handle CORS preflight requests
            return handleOptions(request);
        } else if (
            request.method === "GET" ||
            request.method === "HEAD" ||
            request.method === "POST"
        ) {
            const url = request.url;

            if (url.includes("/inc")) {
                const headers = request.headers;
                let referer = String(headers.get("Referer"));
                if (referer == 'null') {
                    referer = String(headers.get("referer"));
                }
                if (referer == 'null') {
                    referer = "direct";
                }
                else {
                    try {
                        const url = new URL(referer);
                        referer = url.hostname
                    }
                    catch (e) {
                        console.log(e)
                    }
                }

                await IncreasePageViews(referer);

                return new Response('success', {
                    headers: {
                        "content-type": "text/plain",
                        "Access-Control-Allow-Origin": "*",
                        Vary: "Origin",
                    },
                });
            }

            const text =
                "Api is working fine.\n\nSupport : https://telegram.me/TechZBots_Support";

            return new Response(text, {
                headers: {
                    "content-type": "text/plain",
                    "Access-Control-Allow-Origin": "*",
                    Vary: "Origin",
                },
            });
        } else {
            return new Response(null, {
                status: 405,
                statusText: "Method Not Allowed",
            });
        }
    },
};
