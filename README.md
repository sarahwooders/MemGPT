<a href="#user-content-memgpt"><img src="https://memgpt.ai/assets/img/memgpt_logo_circle.png" alt="MemGPT logo" width="75" align="right"></a>

# [MemGPT](https://memgpt.ai)

<div align="center">

 <strong>Try out our MemGPT chatbot on <a href="https://discord.gg/9GEQrxmVyE">Discord</a>!</strong>
 
[![Discord](https://img.shields.io/discord/1161736243340640419?label=Discord&logo=discord&logoColor=5865F2&style=flat-square&color=5865F2)](https://discord.gg/9GEQrxmVyE)
[![arXiv 2310.08560](https://img.shields.io/badge/arXiv-2310.08560-B31B1B?logo=arxiv&style=flat-square)](https://arxiv.org/abs/2310.08560)

</div>

<details open>
  <summary><h2>Create perpetual chatbots 🤖 with self-editing memory!</h1></summary>
  <div align="center">
    <br>
    <img src="https://memgpt.ai/assets/img/demo.gif" alt="MemGPT demo video" width="800">
  </div>
</details>

<details open>
  <summary><h2>Chat with your data 🗃️ - try talking to the <a href="memgpt/personas/examples/docqa">LlamaIndex API docs</a>!</h1></summary>
  <div align="center">
    <img src="https://memgpt.ai/assets/img/docqa_demo.gif" alt="MemGPT demo video for llamaindex api docs search" width="800">
  </div>
  <details>
  <summary><h3>ChatGPT (GPT-4) when asked the same question:</h3></summary>
    <div align="center">
      <img src="https://memgpt.ai/assets/img/llama_index_gpt4.png" alt="GPT-4 when asked about llamaindex api docs" width="800">
    </div>
    (Question from https://github.com/run-llama/llama_index/issues/7756)
  </details>
</details>

## Quick setup 

Join <a href="https://discord.gg/9GEQrxmVyE">Discord</a></strong> and message the MemGPT bot (in the `#memgpt` channel). Then run the following commands (messaged to "MemGPT Bot"): 
* `/profile` (to create your profile)
* `/key` (to enter your OpenAI key)
* `/create` (to create a MemGPT chatbot)

Make sure your privacy settings on this server are open so that MemGPT Bot can DM you: \
MemGPT → Privacy Settings → Direct Messages set to ON
<div align="center">
 <img src="https://memgpt.ai/assets/img/discord/dm_settings.png" alt="set DMs settings on MemGPT server to be open in MemGPT so that MemGPT Bot can message you" width="400">
</div>

You can see the full list of available commands when you enter `/` into the message box. 
<div align="center">
 <img src="https://memgpt.ai/assets/img/discord/slash_commands.png" alt="MemGPT Bot slash commands" width="400">
</div>

## What is MemGPT? 

Memory-GPT (or MemGPT in short) is a system that intelligently manages different memory tiers in LLMs in order to effectively provide extended context within the LLM's limited context window. For example, MemGPT knows when to push critical information to a vector database and when to retrieve it later in the chat, enabling perpetual conversations. Learn more about MemGPT in our [paper](https://arxiv.org/abs/2310.08560). 

## Running MemGPT locally

Install dependencies:

```sh
pip install -r requirements.txt
```

Add your OpenAI API key to your environment:

```sh
# on Linux/Mac
export OPENAI_API_KEY=YOUR_API_KEY
```

```sh
# on Windows
set OPENAI_API_KEY=YOUR_API_KEY
```

To run MemGPT for as a conversation agent in CLI mode, simply run `main.py`:

```sh
python3 main.py
```

To create a new starter user or starter persona (that MemGPT gets initialized with), create a new `.txt` file in [/memgpt/humans/examples](/memgpt/humans/examples) or [/memgpt/personas/examples](/memgpt/personas/examples), then use the `--persona` or `--human` flag when running `main.py`. For example:

```sh
# assuming you created a new file /memgpt/humans/examples/me.txt
python main.py
# Select me.txt during configuration process
```
-- OR --
```sh
# assuming you created a new file /memgpt/humans/examples/me.txt
python main.py --human me.txt
```

### GPT-3.5 support
You can run MemGPT with GPT-3.5 as the LLM instead of GPT-4:
```sh
python main.py
# Select gpt-3.5 during configuration process
```
-- OR --
```sh
python main.py --model gpt-3.5-turbo
```

**Note that this is experimental gpt-3.5-turbo support. It's quite buggy compared to gpt-4, but it should be runnable.**

Please report any bugs you encounter regarding MemGPT running on GPT-3.5 to  https://github.com/cpacker/MemGPT/issues/59.

### Local LLM support
You can run MemGPT with local LLMs too. See [instructions here](/memgpt/local_llm) and report any bugs/improvements here https://github.com/cpacker/MemGPT/discussions/67.

### `main.py` flags
```text
--first
  allows you to send the first message in the chat (by default, MemGPT will send the first message)
--debug
  enables debugging output
```

<details>
<summary>Configure via legacy flags</summary>

```text
--model
  select which model to use ('gpt-4', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo')
--persona
  load a specific persona file
--human
  load a specific human file
--archival_storage_faiss_path=<ARCHIVAL_STORAGE_FAISS_PATH>
  load in document database (backed by FAISS index)
```
</details>


### Interactive CLI commands

These are the commands for the CLI, **not the Discord bot**! The Discord bot has separate commands you can see in Discord by typing `/`.

While using MemGPT via the CLI (not Discord!) you can run various commands:

```text
//
  toggle multiline input mode
/exit
  exit the CLI
/save
  save a checkpoint of the current agent/conversation state
/load
  load a saved checkpoint
/dump
  view the current message log (see the contents of main context)
/memory
  print the current contents of agent memory
/pop
  undo the last message in the conversation
/heartbeat
  send a heartbeat system message to the agent
/memorywarning
  send a memory warning system message to the agent
```

## Use MemGPT to talk to your Database!

MemGPT's archival memory let's you load your database and talk to it! To motivate this use-case, we have included a toy example. 

Consider the `test.db` already included in the repository.

id	| name |	age
--- | --- | ---
1	| Alice |	30
2	| Bob	 | 25
3	| Charlie |	35

To talk to this database, run:

```sh
python main_db.py 
```

And then you can input the path to your database, and your query.

```python
Please enter the path to the database. test.db
...
Enter your message: How old is Bob?
...
🤖 Bob is 25 years old.
```


## Support

If you have any further questions, or have anything to share, we are excited to hear your feedback!

* By default MemGPT will use `gpt-4`, so your API key will require `gpt-4` API access
* For issues and feature requests, please [open a GitHub issue](https://github.com/cpacker/MemGPT/issues) or message us on our `#support` channel on [Discord](https://discord.gg/9GEQrxmVyE)

## Datasets
Datasets used in our [paper](https://arxiv.org/abs/2310.08560) can be downloaded at [Hugging Face](https://huggingface.co/MemGPT).

## 🚀 Project Roadmap
- [x] Release MemGPT Discord bot demo (perpetual chatbot)
- [x] Add additional workflows (load SQL/text into MemGPT external context)
- [x] Integration tests
- [x] Integrate with AutoGen ([discussion](https://github.com/cpacker/MemGPT/discussions/65))
- [x] Add official gpt-3.5-turbo support ([discussion](https://github.com/cpacker/MemGPT/discussions/66))
- [x] CLI UI improvements ([issue](https://github.com/cpacker/MemGPT/issues/11))
- [x] Add support for other LLM backends ([issue](https://github.com/cpacker/MemGPT/issues/18), [discussion](https://github.com/cpacker/MemGPT/discussions/67))
- [ ] Release MemGPT family of open models (eg finetuned Mistral) ([discussion](https://github.com/cpacker/MemGPT/discussions/67))
