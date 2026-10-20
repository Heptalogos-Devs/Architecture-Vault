import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { modelMessageSchema } from 'ai';
import { Liquid } from 'liquidjs';

const readJson = async name => JSON.parse(await readFile(new URL(name, import.meta.url), 'utf8'));
const config = await readJson('./模型与Prompt资源.json');
const fixture = await readJson('./逐步消息预览.json');
const messages = fixture.messages.map(message => modelMessageSchema.parse(message));
assert.deepEqual(messages, fixture.messages);

const engine = new Liquid({
  templates: {}, dynamicPartials: false, relativeReference: false,
  strictVariables: true, strictFilters: true, ownPropertyOnly: true,
  parseLimit: 131072, renderLimit: 100, memoryLimit: 1048576,
});
const baseRoleInstructions = await engine.render(engine.parse(config.promptSave.text), {});
const composeStep = (step, cognition) => ({
  instructions: `${baseRoleInstructions}\n\n${cognition.instructions}`,
  messages: step.messages,
  tools: {},
  toolChoice: 'none',
});

const first = composeStep({ messages }, fixture.contextContribution);
assert.equal(first.messages, messages);
assert.equal(first.messages[1].content[0].toolCallId, first.messages[2].content[0].toolCallId);
const second = composeStep(first, {
  ...fixture.contextContribution,
  instructions: '本步仅核对c0/c1与原材料；店名仍未知。',
});
assert.equal(second.messages, messages);
assert.equal(second.instructions.includes(fixture.contextContribution.instructions), false);

console.log(JSON.stringify({
  prompt: {
    id: config.promptSave.promptId,
    digest: createHash('sha256').update(config.promptSave.text).digest('hex'),
  },
  roleId: 'query_concept_enrichment',
  semanticInputPreview: first,
  semanticBytes: Buffer.byteLength(JSON.stringify(first), 'utf8'),
  nextStepInstructions: second.instructions,
}, null, 2));
