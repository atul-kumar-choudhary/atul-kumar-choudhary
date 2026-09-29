import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'export',
  // Since your repo is atul-kumar-choudhary/atul-kumar-choudhary, GitHub pages will deploy to:
  // https://atul-kumar-choudhary.github.io/atul-kumar-choudhary
  basePath: '/atul-kumar-choudhary',
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
