# Core Knowledge Deficits in Multi-Modal Language Models

**Official website for the ICML 2025 paper submission**

🌐 **Website**: [https://grow-ai-like-a-child.github.io/core-knowledge/](https://grow-ai-like-a-child.github.io/core-knowledge/)  
📄 **Paper**: [https://arxiv.org/abs/2410.10855](https://arxiv.org/abs/2410.10855)  
🤗 **Dataset**: [https://huggingface.co/grow-ai-like-a-child](https://huggingface.co/grow-ai-like-a-child)

## 📖 About

This repository contains the official website for our paper "Core Knowledge Deficits in Multi-Modal Language Models". The website presents our comprehensive evaluation of 230 multi-modal language models using the **CoreCognition** benchmark, which assesses 12 foundational cognitive concepts grounded in developmental cognitive science.

## 🔍 Key Findings

Our research reveals four critical shortcomings in state-of-the-art Multi-modal Large Language Models (MLLMs):
Official Codebase for ICML 2025 paper.
>[__"Core Knowledge Deficits in Multi-Modal Language Models"__](https://arxiv.org/abs/2410.10855)<br>
>Yijiang Li, Qingying Gao, Tianwei Zhao, Bingyang Wang, Haoran Sun, Haiyun Lyu, Dezhi Luo, Hokin Deng<br>
[`[Paper]`](https://arxiv.org/abs/2410.10855) [`[Code]`](https://github.com/williamium3000/core-knowledge) [`[Dataset]`](https://huggingface.co/datasets/williamium/CoreCognition) [`[Website]`](https://grow-ai-like-a-child.github.io/core-knowledge/)

***Abstract.***
> While Multi-modal Large Language Models (MLLMs) demonstrate impressive abilities over high-level perception and reasoning, their robustness in the wild remains limited, often falling short on tasks that are intuitive and effortless for humans. We examine the hypothesis that these deficiencies stem from the absence of core knowledge--rudimentary cognitive abilities innate to humans from early childhood. To explore the core knowledge representation in MLLMs, we introduce CoreCognition, a large-scale benchmark encompassing 12 core knowledge concepts grounded in developmental cognitive science. We evaluate 230 models with 11 different prompts, leading to a total of 2,530 data points for analysis. Our experiments uncover four key findings, collectively demonstrating core knowledge deficits in MLLMs: they consistently underperform and show reduced, or even absent, scalability on low-level abilities relative to high-level ones. Finally, we propose Concept Hacking, a novel controlled evaluation method that reveals MLLMs fail to progress toward genuine core knowledge understanding, but instead rely on shortcut learning as they scale.

![Paper Poster](assets/poster.jpg)

1. **Core Knowledge Deficits**: MLLMs excel at higher-level abilities but struggle with lower-level cognitive abilities
2. **Misaligned Dependency**: Core abilities show weak cross-stage correlations, lacking developmental scaffolding
3. **Predictability**: Performance on core knowledge predicts higher-level abilities
4. **Limited Scaling**: MLLMs show minimal scalability improvements on low-level abilities compared to high-level ones

## 🧠 CoreCognition Benchmark

The **CoreCognition** benchmark evaluates twelve foundational cognitive concepts:

1. **Permanence** - Objects persist when not perceived
2. **Continuity** - Objects remain unified across space and time
3. **Boundary** - Transitions between objects
4. **Spatiality** - Understanding Euclidean properties
5. **Perceptual Constancy** - Appearance changes ≠ property changes
6. **Intuitive Physics** - Laws of physical interaction
7. **Perspective** - Seeing what others see
8. **Hierarchy** - Inclusion/exclusion of objects and categories
9. **Conservation** - Property invariances despite transformations
10. **Tool Use** - Manipulating objects to achieve goals
11. **Intentionality** - Understanding what others want
12. **Mechanical Reasoning** - Inferring actions from system states

## 🔬 Concept Hacking

We introduce **Concept Hacking**, a novel controlled evaluation method that systematically manipulates task-relevant features while preserving task-irrelevant conditions. This reveals that MLLMs fail to develop genuine core knowledge understanding and instead rely on shortcut learning as they scale.

## 📊 Evaluation Scale

- **230 MLLMs** evaluated across different model families and sizes
- **11 different prompts** to ensure robust evaluation
- **>26,000 total judgments** across all models and tasks
- **2,530 image-question pairs** in the benchmark

## 🏗️ Website Structure

```
├── _config.yml              # Jekyll configuration
├── _layouts/
│   └── default.html         # Main layout template
├── index.html               # Homepage with full paper content
├── assets/
│   ├── images/              # Paper figures and illustrations
│   ├── growai.png          # Site favicon
│   └── favicon.svg         # Backup favicon
├── Gemfile                  # Ruby dependencies
└── README.md               # This file
```

## 🚀 Local Development

To run the website locally:

```bash
# Install dependencies
gem install jekyll bundler
bundle install

# Serve the site locally
bundle exec jekyll serve --livereload
```

Then visit: `http://localhost:4000/core-knowledge`

## 👥 Authors

**Yijiang Li¹**, **Qingying Gao²,§**, **Tianwei Zhao²,§**, **Bingyang Wang³,§**, **Haoran Sun²**, **Haiyun Lyu⁴**, **Robert D. Hawkins⁵**, **Nuno Vasconcelos¹**, **Tal Golan⁶**, **Dezhi Luo⁷,⁸,†**, **Hokin Deng⁹,†**

¹University of California San Diego, ²Johns Hopkins University, ³Emory University, ⁴University of North Carolina at Chapel Hill, ⁵Stanford University, ⁶Ben-Gurion University of the Negev, ⁷University of Michigan, ⁸University College London, ⁹Carnegie Mellon University

§Equal Contribution, †Corresponding author

## 📄 Citation

If you find this work useful in your research, please consider citing:

```bibtex
@article{li2025core,
    title={Core Knowledge Deficits in Multi-Modal Language Models}, 
    author={Li, Yijiang and Gao, Qingying and Zhao, Tianwei and Wang, Bingyang and Sun, Haoran and Lyu, Haiyun and Luo, Dezhi and Deng, Hokin},
    journal={arXiv preprint arXiv:2410.10855},
    year={2025}
}
```


## 🔧 Technical Details

The website is built with:
- **Jekyll** for static site generation
- **Tailwind CSS** for styling
- **GitHub Pages** for hosting
- **Responsive design** optimized for all devices
- **SEO optimization** for better discoverability

---

*This website presents the official results and findings from our comprehensive evaluation of multi-modal language models on core cognitive abilities.*
