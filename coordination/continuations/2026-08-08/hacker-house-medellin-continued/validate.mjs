import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const expectedArchiveSha = "93f08a123f38ffdc7a99abee809ccc8348c00442868c14edb79f8bbd669a443b";
const secretPatterns = [
  /ghp_[A-Za-z0-9]{20,}/,
  /github_pat_[A-Za-z0-9_]{20,}/,
  /lin_api_[A-Za-z0-9]{20,}/,
  /cfat_[A-Za-z0-9_-]{20,}/,
  /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/,
];

async function walk(directory) {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await walk(fullPath));
    else files.push(fullPath);
  }
  return files;
}

const files = await walk(root);
for (const file of files.filter((candidate) => candidate.endsWith(".json"))) {
  JSON.parse(await readFile(file, "utf8"));
}

for (const required of [
  "README.md",
  "ORIGINAL_ARCHIVE.sha256",
  "LIVE_RECONCILIATION.md",
  "agent-bridge.live.json",
  "original/FINAL_STATUS.md",
  "original/GITHUB_STATUS.md",
  "original/LINEAR_STATUS.md",
  "original/CLOUDFLARE_STATUS.md",
  "original/coordination/agent-bridge.json",
  "original/coordination/handoffs/hhm-e2e.json",
  "original/coordination/handoffs/hhm-monorepo.json",
  "proposed-hhm-monorepo/.gitmodules",
  "proposed-hhm-monorepo/repos.json",
  "proposed-hhm-monorepo/gitlinks.json",
]) {
  await stat(path.join(root, required));
}

const checksum = await readFile(path.join(root, "ORIGINAL_ARCHIVE.sha256"), "utf8");
if (!checksum.startsWith(`${expectedArchiveSha}  hacker-house-medellin-continued.zip`)) {
  throw new Error("archive checksum drift");
}

const gitmodules = await readFile(path.join(root, "proposed-hhm-monorepo/.gitmodules"), "utf8");
if (!gitmodules.includes("url = ../hhm-e2e.git")) throw new Error("relative submodule URL drift");

for (const file of files) {
  let text;
  try {
    text = await readFile(file, "utf8");
  } catch {
    continue;
  }
  for (const pattern of secretPatterns) {
    if (pattern.test(text)) {
      throw new Error(`credential-shaped value found in ${path.relative(root, file)}`);
    }
  }
}

console.log("validated Hacker House Medellín continuation evidence and fail-closed handoff");
