---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<script>
function toggleBibtex(id) {
    const element = document.getElementById(id);
    if (element.style.display === "none" || element.style.display === "") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}
</script>

<style>
.bibtex-block {
    display: none;
    background: #f5f5f5;
    padding: 15px;
    margin: 10px 0;
    border-radius: 4px;
    font-family: monospace;
    white-space: pre-wrap;
    font-size: 0.85em;
}

.bibtex-link {
    text-decoration: none;
    cursor: pointer;
}

/* publication styling */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.pub-title {
    font-weight: bold;
}

.pub-conf {
    font-style: italic;
}

.pub-authors {
    font-weight: normal;
}

.pub-authors u {
    text-decoration: underline;
}
.pub-entry {
    margin-bottom: 2em;
    /* space for 50px-high thumbnail on left */
    padding-left: 60px;
    background-repeat: no-repeat;
    background-size: auto 50px;
    background-position: left center;
}
.pub-links {
    margin: 0.5em 0;
}
.pub-button {
    display: inline-block;
    padding: 0.2em 0.5em;
    margin-right: 0.25em;
    border: 1px solid #000;
    background-color: #fff;
    color: #000;
    text-decoration: none;
    text-transform: lowercase;
    font-size: 0.9em;
}
.pub-button:hover {
    background-color: #f0f0f0;
}
.publications-heading {
    font-size: 1.75em;
    margin-bottom: 0.5em;
}
</style>

Hi, I'm Ori! I'm a graduate student at the University of Tübingen and the International Max Planck Research School for Intelligent Systems (IMPRS-IS), working in [Matthias Bethge's lab](https://bethgelab.org). 

I'm interested in closing the gap between how machine learning models perform in known benchmarks versus their performance in more complicated real-world scenarios. During my PhD, I had the privilege of collaborating with [Ravid Shwartz-Ziv](https://www.ravid-shwartz-ziv.com/), [Yann LeCun](http://yann.lecun.com/), and [Ofir Press](https://ofir.io/).
 

Previously, I graduated from Tel Aviv University with a BSc in Mathematics and an MSc in Computer Science, advised by [Lior Wolf](https://www.cs.tau.ac.il/~wolf/).

My brother [Ofir Press](https://ofir.io/) is a machine learning researcher.

<h2 class="publications-heading">Publications</h2>
<div class="publications">
  <div class="pub-entry" style="background-image: url('/assets/thumb-algotune.png');">
    <strong class="pub-title">AlgoTune: Can Language Models Speed Up General-Purpose Numerical Programs?</strong><br>
    <span class="pub-authors"><u>Ori Press</u>, Brandon Amos, Haoyu Zhao, Yikai Wu, Samuel Ainsworth, Dominik Krupke, Patrick Kidger, Touqir Sajed, Bartolomeo Stellato, Jisun Park, Nathanael Bosch, Eli Meril, Albert Steppi, Arman Zharmagambetov, Fangzhao Zhang, David Pérez–Piñeiro, Alberto Mercurio, Ni Zhan, Talor Abramovich, Kilian Lieret, Hanlin Zhang, Shirley Huang, Matthias Bethge, Ofir Press</span><br>
    <em class="pub-conf">Preprint, 2025</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://www.algotune.io/paper.pdf">Paper</a>
      <a class="pub-button" href="https://www.algotune.io">Website</a>
    </div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-humanitysexam.png');">
    <strong class="pub-title">Humanity's Last Exam</strong><br>
    <span class="pub-authors">Long Phan, Alice Gatti, Ziwen Han, …, <u>Ori Press</u>, … *(contributed 6 questions, 1 in the top 550)*</span><br>
    <em class="pub-conf">Preprint, 2025</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://arxiv.org/abs/2501.14249">Paper</a>
      <a class="pub-button" href="https://agi.safe.ai/">Website</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-humanitysexam')">Bibtex</a>
    </div>
    <div id="bibtex-humanitysexam" class="bibtex-block">@misc{phan2025humanitysexam,
  title={Humanity's Last Exam},
  author={Long Phan and Alice Gatti and Ziwen Han and Nathaniel Li and Josephina Hu and Hugh Zhang and Sean Shi and Michael Choi and Anish Agrawal and Arnav Chopra and Adam Khoja and Ryan Kim and Jason Hausenloy and Oliver Zhang and Mantas Mazeika and Daron Anderson and Tung Nguyen and Mobeen Mahmood and Fiona Feng and Steven Y. Feng and Haoran Zhao and Michael Yu and Varun Gangal and Chelsea Zou and Zihan Wang and Jessica P. Wang and Pawan Kumar and Oleksandr Pokutnyi and Robert Gerbicz and Serguei Popov and John-Clark Levin and Mstyslav Kazakov and Johannes Schmitt and Geoff Galgon and Alvaro Sanchez and Yongki Lee and Will Yeadon and Scott Sauers and Marc Roth and Chidozie Agu and Søren Riis and Fabian Giska and Saiteja Utpala and Zachary Giboney and Gashaw M. Goshu and Joan of Arc Xavier and Sarah-Jane Crowson and Mohinder Maheshbhai Naiya and Noah Burns and Lennart Finke and Zerui Cheng and Hyunwoo Park and Francesco Fournier-Facio and John Wydallis and Mark Nandor and Ankit Singh and Tim Gehrunger and Jiaqi Cai and Ben McCarty and Darling Duclosel and Jungbae Nam and Jennifer Zampese and Ryan G. Hoerr and Aras Bacho and Gautier Abou Loume and Abdallah Galal and Hangrui Cao and Alexis C Garretson and Damien Sileo and Qiuyu Ren and Doru Cojoc and Pavel Arkhipov and Usman Qazi and Lianghui Li and Sumeet Motwani and Christian Schroeder de Witt and Edwin Taylor and Johannes Veith and Eric Singer and Taylor D. Hartman and Paolo Rissone and Jaehyeok Jin and Jack Wei Lun Shi and Chris G. Willcocks and Joshua Robinson and Aleksandar Mikov and Ameya Prabhu and Longke Tang and Xavier Alapont and Justine Leon Uro and Kevin Zhou and Emily de Oliveira Santos and Andrey Pupasov Maksimov and Edward Vendrow and Kengo Zenitani and Julien Guillod and Yuqi Li and Joshua Vendrow and Vladyslav Kuchkin and Ng Ze-An and Pierre Marion and Denis Efremov and Jayson Lynch and Kaiqu Liang and Andrew Gritsevskiy and Dakotah Martinez and Ben Pageler and Nick Crispino and Dimitri Zvonkine and Natanael Wildner Fraga and Saeed Soori and Ori Press and Henry Tang and Julian Salazar and Sean R. Green and Lina Brüssel and Moon Twayana and Aymeric Dieuleveut and T. Ryan Rogers and Wenjin Zhang and Bikun Li and Jinzhou Yang and Arun Rao and Gabriel Loiseau and Mikhail Kalinin and Marco Lukas and Ciprian Manolescu and Subrata Mishra and Ariel Ghislain Kemogne Kamdoum and Tobias Kreiman and Tad Hogg and Alvin Jin and Carlo Bosio and Gongbo Sun and Brian P Coppola and Tim Tarver and Haline Heidinger and Rafael Sayous and Stefan Ivanov and Joseph M Cavanagh and Jiawei Shen and Joseph Marvin Imperial and Philippe Schwaller and Shaipranesh Senthilkuma and Andres M Bran and Ali Dehghan and Andres Algaba and Brecht Verbeken and David Noever and Ragavendran P V and Lisa Schut and Ilia Sucholutsky and Evgenii Zheltonozhskii and Derek Lim and Richard Stanley and Shankar Sivarajan and Tong Yang and John Maar and Julian Wykowski and Martí Oller and Jennifer Sandlin and Anmol Sahu and Yuzheng Hu and Sara Fish and Nasser Heydari and Archimedes Apronti and Kaivalya Rawal and Tobias Garcia Vilchis and Yuexuan Zu and Martin Lackner and James Koppel and Jeremy Nguyen and Daniil S. Antonenko and Steffi Chern and Bingchen Zhao and Pierrot Arsene and Alan Goldfarb and Sergey Ivanov and Rafał Poświata and Chenguang Wang and Daofeng Li and Donato Crisostomi and Andrea Achilleos and Benjamin Myklebust and Archan Sen and David Perrella and Nurdin Kaparov and Mark H Inlow and Allen Zang and Elliott Thornley and Daniil Orel and Vladislav Poritski and Shalev Ben-David and Zachary Berger and Parker Whitfill and Michael Foster and Daniel Munro and Linh Ho and Dan Bar Hava and Aleksey Kuchkin and Robert Lauff and David Holmes and Frank Sommerhage and Keith Schneider and Zakayo Kazibwe and Nate Stambaugh and Mukhwinder Singh and Ilias Magoulas and Don Clarke and Dae Hyun Kim and Felipe Meneguitti Dias and Veit Elser and Kanu Priya Agarwal and Victor Efren Guadarrama Vilchis and Immo Klose and Christoph Demian and Ujjwala Anantheswaran and Adam Zweiger and Guglielmo Albani and Jeffery Li and Nicolas Daans and Maksim Radionov and Václav Rozhoň and Ziqiao Ma and Christian Stump and Mohammed Berkani and Jacob Platnick and Volodymyr Nevirkovets and Luke Basler and Marco Piccardo and Ferenc Jeanplong and Niv Cohen and Josef Tkadlec and Paul Rosu and Piotr Padlewski and Stanislaw Barzowski and Kyle Montgomery and Aline Menezes and Arkil Patel and Zixuan Wang and Jamie Tucker-Foltz and Jack Stade and Tom Goertzen and Fereshteh Kazemi and Jeremiah Milbauer and John Arnold Ambay and Abhishek Shukla and Yan Carlos Leyva Labrador and Alan Givré and Hew Wolff and Vivien Rossbach and Muhammad Fayez Aziz and Younesse Kaddar and Yanxu Chen and Robin Zhang and Jiayi Pan and Antonio Terpin and Niklas Muennighoff and Hailey Schoelkopf and Eric Zheng and Avishy Carmi and Adam Jones and Jainam Shah and Ethan D. L. Brown and Kelin Zhu and Max Bartolo and Richard Wheeler and Andrew Ho and Shaul Barkan and Jiaqi Wang and Martin Stehberger and Egor Kretov and Kaustubh Sridhar and Zienab EL-Wasif and Anji Zhang and Daniel Pyda and Joanna Tam and David M. Cunningham and Vladimir Goryachev and Demosthenes Patramanis and Michael Krause and Andrew Redenti and Daniel Bugas and David Aldous and Jesyin Lai and Shannon Coleman and Mohsen Bahaloo and Jiangnan Xu and Sangwon Lee and Sandy Zhao and Ning Tang and Michael K. Cohen and Micah Carroll and Orr Paradise and Jan Hendrik Kirchner and Stefan Steinerberger and Maksym Ovchynnikov and Jason O. Matos and Adithya Shenoy and Benedito Alves de Oliveira Junior and Michael Wang and Yuzhou Nie and Paolo Giordano and Philipp Petersen and Anna Sztyber-Betley and Priti Shukla and Jonathan Crozier and Antonella Pinto and Shreyas Verma and Prashant Joshi and Zheng-Xin Yong and Allison Tee and Jérémy Andréoletti and Orion Weller and Raghav Singhal and Gang Zhang and Alexander Ivanov and Seri Khoury and Hamid Mostaghimi and Kunvar Thaman and Qijia Chen and Tran Quoc Khánh and Jacob Loader and Stefano Cavalleri and Hannah Szlyk and Zachary Brown and Jonathan Roberts and William Alley and Kunyang Sun and Ryan Stendall and Max Lamparth and Anka Reuel and Ting Wang and Hanmeng Xu and Sreenivas Goud Raparthi and Pablo Hernández-Cámara and Freddie Martin and Dmitry Malishev and Thomas Preu and Tomek Korbak and Marcus Abramovitch and Dominic Williamson and Ziye Chen and Biró Bálint and M Saiful Bari and Peyman Kassani and Zihao Wang and Behzad Ansarinejad and Laxman Prasad Goswami and Yewen Sun and Hossam Elgnainy and Daniel Tordera and George Balabanian and Earth Anderson and Lynna Kvistad and Alejandro José Moyano and Rajat Maheshwari and Ahmad Sakor and Murat Eron and Isaac C. McAlister and Javier Gimenez and Innocent Enyekwe and Andrew Favre D. O. and Shailesh Shah and Xiaoxiang Zhou and Firuz Kamalov and Ronald Clark and Sherwin Abdoli and Tim Santens and Khalida Meer and Harrison K Wang and Kalyan Ramakrishnan and Evan Chen and Alessandro Tomasiello and G. Bruno De Luca and Shi-Zhuo Looi and Vinh-Kha Le and Noam Kolt and Niels Mündler and Avi Semler and Emma Rodman and Jacob Drori and Carl J Fossum and Milind Jagota and Ronak Pradeep and Honglu Fan and Tej Shah and Jonathan Eicher and Michael Chen and Kushal Thaman and William Merrill and Carter Harris and Jason Gross and Ilya Gusev and Asankhaya Sharma and Shashank Agnihotri and Pavel Zhelnov and Siranut Usawasutsakorn and Mohammadreza Mofayezi and Sergei Bogdanov and Alexander Piperski and Marc Carauleanu and David K. Zhang and Dylan Ler and Roman Leventov and Ignat Soroko and Thorben Jansen and Pascal Lauer and Joshua Duersch and Vage Taamazyan and Wiktor Morak and Wenjie Ma and William Held and Tran Đuc Huy and Ruicheng Xian and Armel Randy Zebaze and Mohanad Mohamed and Julian Noah Leser and Michelle X Yuan and Laila Yacar and Johannes Lengler and Hossein Shahrtash and Edson Oliveira and Joseph W. Jackson and Daniel Espinosa Gonzalez and Andy Zou and Muthu Chidambaram and Timothy Manik and Hector Haffenden and Dashiell Stander and Ali Dasouqi and Alexander Shen and Emilien Duc and Bita Golshani and David Stap and Mikalai Uzhou and Alina Borisovna Zhidkovskaya and Lukas Lewark and Mátyás Vincze and Dustin Wehr and Colin Tang and Zaki Hossain and Shaun Phillips and Jiang Muzhen and Fredrik Ekström and Angela Hammon and Oam Patel and Nicolas Remy and Faraz Farhidi and George Medley and Forough Mohammadzadeh and Madellene Peñaflor and Haile Kassahun and Alena Friedrich and Claire Sparrow and Taom Sakal and Omkar Dhamane and Ali Khajegili Mirabadi and Eric Hallman and Mike Battaglia and Mohammad Maghsoudimehrabani and Hieu Hoang and Alon Amit and Dave Hulbert and Roberto Pereira and Simon Weber and Stephen Mensah and Nathan Andre and Anton Peristyy and Chris Harjadi and Himanshu Gupta and Stephen Malina and Samuel Albanie and Will Cai and Mustafa Mehkary and Frank Reidegeld and Anna-Katharina Dick and Cary Friday and Jasdeep Sidhu and Wanyoung Kim and Mariana Costa and Hubeyb Gurdogan and Brian Weber and Harsh Kumar and Tong Jiang and Arunim Agarwal and Chiara Ceconello and Warren S. Vaz and Chao Zhuang and Haon Park and Andrew R. Tawfeek and Daattavya Aggarwal and Michael Kirchhof and Linjie Dai and Evan Kim and Johan Ferret and Yuzhou Wang and Minghao Yan and Krzysztof Burdzy and Lixin Zhang and Antonio Franca and Diana T. Pham and Kang Yong Loh and Joshua Robinson and Shreen Gul and Gunjan Chhablani and Zhehang Du and Adrian Cosma and Colin White and Robin Riblet and Prajvi Saxena and Jacob Votava and Vladimir Vinnikov and Ethan Delaney and Shiv Halasyamani and Syed M. Shahid and Jean-Christophe Mourrat and Lavr Vetoshkin and Renas Bacho and Vincent Ginis and Aleksandr Maksapetyan and Florencia de la Rosa and Xiuyu Li and Guillaume Malod and Leon Lang and Julien Laurendeau and Fatimah Adesanya and Julien Portier and Lawrence Hollom and Victor Souza and Yuchen Anna Zhou and Yiğit Yalın and Gbenga Daniel Obikoya and Luca Arnaboldi and Rai and Filippo Bigi and Kaniuar Bacho and Pierre Clavier and Gabriel Recchia and Mara Popescu and Nikita Shulga and Ngefor Mildred Tanwie and Thomas C. H. Lux and Ben Rank and Colin Ni and Alesia Yakimchyk and Huanxu and Liu and Olle Häggström and Emil Verkama and Himanshu Narayan and Hans Gundlach and Leonor Brito-Santana and Brian Amaro and Vivek Vajipey and Rynaa Grover and Yiyang Fan and Gabriel Poesia Reis e Silva and Linwei Xin and Yosi Kratish and Jakub Łucki and Wen-Ding Li and Justin Xu and Kevin Joseph Scaria and Freddie Vargus and Farzad Habibi and Long and Lian and Emanuele Rodolà and Jules Robins and Vincent Cheng and Declan Grabb and Ida Bosio and Tony Fruhauff and Ido Akov and Eve J. Y. Lo and Hao Qi and Xi Jiang and Ben Segev and Jingxuan Fan and Sarah Martinson and Erik Y. Wang and Kaylie Hausknecht and Michael P. Brenner and Mao Mao and Yibo Jiang and Xinyu Zhang and David Avagian and Eshawn Jessica Scipio and Muhammad Rehan Siddiqi and Alon Ragoler and Justin Tan and Deepakkumar Patil and Rebeka Plecnik and Aaron Kirtland and Roselynn Grace Montecillo and Stephane Durand and Omer Faruk Bodur and Zahra Adoul and Mohamed Zekry and Guillaume Douville and Ali Karakoc and Tania C. B. Santos and Samir Shamseldeen and Loukmane Karim and Anna Liakhovitskaia and Nate Resman and Nicholas Farina and Juan Carlos Gonzalez and Gabe Maayan and Sarah Hoback and Rodrigo De Oliveira Pena and Glen Sherman and Hodjat Mariji and Rasoul Pouriamanesh and Wentao Wu and Gözdenur Demir and Sandra Mendoza and Ismail Alarab and Joshua Cole and Danyelle Ferreira and Bryan Johnson and Hsiaoyun Milliron and Mohammad Safdari and Liangti Dai and Siriphan Arthornthurasuk and Alexey Pronin and Jing Fan and Angel Ramirez-Trinidad and Ashley Cartwright and Daphiny Pottmaier and Omid Taheri and David Outevsky and Stanley Stepanic and Samuel Perry and Luke Askew and Raúl Adrián Huerta Rodríguez and Abdelkader Dendane and Sam Ali and Ricardo Lorena and Krishnamurthy Iyer and Sk Md Salauddin and Murat Islam and Juan Gonzalez and Josh Ducey and Russell Campbell and Maja Somrak and Vasilios Mavroudis and Eric Vergo and Juehang Qin and Benjámin Borbás and Eric Chu and Jack Lindsey and Anil Radhakrishnan and Antoine Jallon and I. M. J. McInnis and Alex Hoover and Sören Möller and Song Bian and John Lai and Tejal Patwardhan and Summer Yue and Alexandr Wang and Dan Hendrycks}
  year={2025},
  eprint={2501.14249},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2501.14249},
}</div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-swebench.png');">
    <strong class="pub-title">SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?</strong><br>
    <span class="pub-authors">John Yang*, Carlos E. Jimenez*, Alex L. Zhang, Kilian Lieret, Joyce Yang, Xindi Wu, <u>Ori Press</u>, Niklas Muennighoff, Gabriel Synnaeve, Karthik Narasimhan, Diyi Yang, Sida I. Wang, Ofir Press</span><br>
    <em class="pub-conf">International Conference on Learning Representations, 2025</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://www.swebench.com/assets/paper.pdf">Paper</a>
      <a class="pub-button" href="https://www.swebench.com/multimodal">Website</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-swebench')">Bibtex</a>
    </div>
    <div id="bibtex-swebench" class="bibtex-block">@inproceedings{yang2025swebench,
  title={SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?},
  author={Yang, John and Jimenez, Carlos E. and Zhang, Alex L. and Lieret, Kilian and Yang, Joyce and Wu, Xindi and Press, Ori and Muennighoff, Niklas and Synnaeve, Gabriel and Narasimhan, Karthik and Yang, Diyi and Wang, Sida I. and Press, Ofir},
  booktitle={International Conference on Learning Representations},
  year={2025},
  url={https://arxiv.org/abs/2410.03859},
  note={Available at \url{https://www.swebench.com/multimodal}}
}</div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-citeme.png');">
    <strong class="pub-title">CiteME: Can Language Models Accurately Cite Scientific Claims?</strong><br>
    <span class="pub-authors"><u>Ori Press</u>*, Andreas Hochlehnert*, Ameya Prabhu, Vishaal Udandarao, Ofir Press‡, Matthias Bethge‡ (*/‡ shared first/last authorship)</span><br>
    <em class="pub-conf">Neural Information Processing Systems, 2024</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://arxiv.org/pdf/2407.12861">Paper</a>
      <a class="pub-button" href="https://github.com/bethgelab/CiteME/">Code</a>
      <a class="pub-button" href="https://citeme.ai">Website</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-citeme')">Bibtex</a>
    </div>
    <div id="bibtex-citeme" class="bibtex-block">@article{press2024citeme,
  title={CiteME: Can Language Models Accurately Cite Scientific Claims?},
  author={Press, Ori and Hochlehnert, Andreas and Prabhu, Ameya and Udandarao, Vishaal and Press, Ofir and Bethge, Matthias},
  journal={Advances in Neural Information Processing Systems},
  volume={37},
  pages={7847--7877},
  year={2024}
}</div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-entropy.png');">
    <strong class="pub-title">The Entropy Enigma: Success and Failure of Entropy Minimization</strong><br>
    <span class="pub-authors"><u>Ori Press</u>, Ravid Shwartz-Ziv, Yann LeCun, Matthias Bethge</span><br>
    <em class="pub-conf">International Conference on Machine Learning, 2024</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://arxiv.org/pdf/2405.05012">Paper</a>
      <a class="pub-button" href="https://github.com/oripress/EntropyEnigma">Code</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-entropy')">Bibtex</a>
    </div>
    <div id="bibtex-entropy" class="bibtex-block">@inproceedings{press2024entropy,
  title     = {The Entropy Enigma: Success and Failure of Entropy Minimization},
  author    = {Press, Ori and Shwartz-Ziv, Ravid and LeCun, Yann and Bethge, Matthias},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  year      = {2024},
  volume    = {235},
  pages     = {41064--41085},
  publisher = {PMLR},
  address   = {Vienna, Austria},
  url       = {https://proceedings.mlr.press/v235/press24a.html},
  pdf       = {https://raw.githubusercontent.com/mlresearch/v235/main/assets/press24a/press24a.pdf},
  note      = {Code available at \url{https://github.com/oripress/EntropyEnigma}}
}

</div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-rdumb.png');">
    <strong class="pub-title">RDumb: A simple approach that questions our progress in continual test-time adaptation</strong><br>
    <span class="pub-authors"><u>Ori Press</u>, Steffen Schneider, Matthias Kümmerer, Matthias Bethge</span><br>
    <em class="pub-conf">Neural Information Processing Systems, 2023</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://arxiv.org/abs/2306.05401">Paper</a>
      <a class="pub-button" href="https://github.com/oripress/CCC">Code</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-rdumb')">Bibtex</a>
    </div>
    <div id="bibtex-rdumb" class="bibtex-block">@article{press2023rdumb,
  title={Rdumb: A simple approach that questions our progress in continual test-time adaptation},
  author={Press, Ori and Schneider, Steffen and K{\"u}mmerer, Matthias and Bethge, Matthias},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  pages={39915--39935},
  year={2023}
}
</div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-calibrated.png');">
    <strong class="pub-title">Calibrated prediction in and out-of-domain for state-of-the-art saliency modeling</strong><br>
    <span class="pub-authors">Akis Linardos*, Matthias Kümmerer*, <u>Ori Press</u>, Matthias Bethge</span><br>
    <em class="pub-conf">International Conference on Computer Vision, 2021</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://arxiv.org/pdf/2105.12441.pdf">Paper</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-calibrated')">Bibtex</a>
    </div>
    <div id="bibtex-calibrated" class="bibtex-block">@inproceedings{linardos2021deepgaze,
  title={DeepGaze IIE: Calibrated prediction in and out-of-domain for state-of-the-art saliency modeling},
  author={Linardos, Akis and K{\"u}mmerer, Matthias and Press, Ori and Bethge, Matthias},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={12919--12928},
  year={2021}
}</div>
  </div>
  <div class="pub-entry" style="background-image: url('/assets/thumb-emerging.png');">
    <strong class="pub-title">Emerging Disentanglement in Auto-Encoder Based Unsupervised Image Content Transfer</strong><br>
    <span class="pub-authors"><u>Ori Press</u>, Tomer Galanti, Sagie Benaim, Lior Wolf</span><br>
    <em class="pub-conf">International Conference on Learning Representations, 2019</em><br>
    <div class="pub-links">
      <a class="pub-button" href="https://openreview.net/pdf?id=BylE1205Fm">Paper</a>
      <a class="pub-button" href="https://github.com/oripress/ContentDisentanglement">Code</a>
      <a class="pub-button bibtex-link" onclick="toggleBibtex('bibtex-emerging')">Bibtex</a>
    </div>
    <div id="bibtex-emerging" class="bibtex-block">@inproceedings{press2019disentanglement,
  title={Emerging Disentanglement in Auto-Encoder Based Unsupervised Image Content Transfer},
  author={Press, Ori and Galanti, Tomer and Benaim, Sagie and Wolf, Lior},
  booktitle={International Conference on Learning Representations},
  year={2019},
  url={https://openreview.net/pdf?id=BylE1205Fm},
  note={Available at \url{https://github.com/oripress/ContentDisentanglement}}
}</div>
  </div>
</div>

### Contact me

[ori.press@bethgelab.org](mailto:ori.press@bethgelab.org)
