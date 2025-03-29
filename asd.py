from bs4 import BeautifulSoup

html = """
<ul id="terms-list">
        <li data-frequency="398023" data-relevance="515" data-term="rock" data-encoded-term="rock" data-term-stats="1	19.8	0.000	398023	cn5,ol,wiki,wn|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="/rock">rock</a>
          </span>
          <span class="term-help" data-term="rock"><a href="/pebble#define=rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="296814" data-relevance="514" data-term="stone" data-encoded-term="stone" data-term-stats="1	23.0	0.000	296814	cn5,ol,wn|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="/stone">stone</a>
          </span>
          <span class="term-help" data-term="stone"><a href="/pebble#define=stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="18089" data-relevance="513" data-term="gravel" data-encoded-term="gravel" data-term-stats="1	7.9	0.000	18089	cn5,ol|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="/gravel">gravel</a>
          </span>
          <span class="term-help" data-term="gravel"><a href="/pebble#define=gravel" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="23277" data-relevance="512" data-term="boulder" data-encoded-term="boulder" data-term-stats="1	8.9	0.000	23277	cn5,ol|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="/boulder">boulder</a>
          </span>
          <span class="term-help" data-term="boulder"><a href="/pebble#define=boulder" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="28451" data-relevance="511" data-term="granite" data-encoded-term="granite" data-term-stats="1	4.0	0.000	28451	cn5,ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="/granite">granite</a>
          </span>
          <span class="term-help" data-term="granite"><a href="/pebble#define=granite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="15498" data-relevance="510" data-term="stony" data-encoded-term="stony" data-term-stats="1	3.6	0.000	15498	cn5,ol|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="/stony">stony</a>
          </span>
          <span class="term-help" data-term="stony"><a href="/pebble#define=stony" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="10381" data-relevance="509" data-term="conglomerate" data-encoded-term="conglomerate" data-term-stats="1	2.3	0.000	10381	wiki,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/conglomerate" onclick="window.location=this.dataset.href" rel="nofollow">conglomerate</a>
          </span>
          <span class="term-help" data-term="conglomerate"><a href="/pebble#define=conglomerate" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="38" data-relevance="508" data-term="clastic rock" data-encoded-term="clastic%20rock" data-term-stats="1	2.7	0.000	38	cn5,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/clastic-rock" onclick="window.location=this.dataset.href" rel="nofollow">clastic rock</a>
          </span>
          <span class="term-help" data-term="clastic rock"><a href="/pebble#define=clastic rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="825" data-relevance="507" data-term="pumice" data-encoded-term="pumice" data-term-stats="1	2.0	0.000	825	cn5,ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pumice" onclick="window.location=this.dataset.href" rel="nofollow">pumice</a>
          </span>
          <span class="term-help" data-term="pumice"><a href="/pebble#define=pumice" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="964" data-relevance="506" data-term="particle size" data-encoded-term="particle%20size" data-term-stats="1	2.6	0.000	964	wiki,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/particle-size" onclick="window.location=this.dataset.href" rel="nofollow">particle size</a>
          </span>
          <span class="term-help" data-term="particle size"><a href="/pebble#define=particle size" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1423" data-relevance="505" data-term="tufa" data-encoded-term="tufa" data-term-stats="1	2.2	0.000	1423	cn5,ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tufa" onclick="window.location=this.dataset.href" rel="nofollow">tufa</a>
          </span>
          <span class="term-help" data-term="tufa"><a href="/pebble#define=tufa" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1486" data-relevance="504" data-term="cobble" data-encoded-term="cobble" data-term-stats="1	2.2	0.000	1486	ol,wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cobble" onclick="window.location=this.dataset.href" rel="nofollow">cobble</a>
          </span>
          <span class="term-help" data-term="cobble"><a href="/pebble#define=cobble" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3415" data-relevance="503" data-term="pebbles" data-encoded-term="pebbles" data-term-stats="0	2.0	0.000	3415	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pebbles" onclick="window.location=this.dataset.href" rel="nofollow">pebbles</a>
          </span>
          <span class="term-help" data-term="pebbles"><a href="/pebble#define=pebbles" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="525" data-relevance="502" data-term="metamorphic rock" data-encoded-term="metamorphic%20rock" data-term-stats="1	1.9	0.000	525	cn5,ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/metamorphic-rock" onclick="window.location=this.dataset.href" rel="nofollow">metamorphic rock</a>
          </span>
          <span class="term-help" data-term="metamorphic rock"><a href="/pebble#define=metamorphic rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5088" data-relevance="501" data-term="boulders" data-encoded-term="boulders" data-term-stats="0	2.0	0.000	5088	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/boulders" onclick="window.location=this.dataset.href" rel="nofollow">boulders</a>
          </span>
          <span class="term-help" data-term="boulders"><a href="/pebble#define=boulders" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1639" data-relevance="500" data-term="palaeolithic" data-encoded-term="palaeolithic" data-term-stats="1	1.8	0.000	1639	wiki,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/palaeolithic" onclick="window.location=this.dataset.href" rel="nofollow">palaeolithic</a>
          </span>
          <span class="term-help" data-term="palaeolithic"><a href="/pebble#define=palaeolithic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="8423" data-relevance="499" data-term="egg shaped" data-encoded-term="egg%20shaped" data-term-stats="0	1.8	0.000	8423	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/egg-shaped" onclick="window.location=this.dataset.href" rel="nofollow">egg shaped</a>
          </span>
          <span class="term-help" data-term="egg shaped"><a href="/pebble#define=egg shaped" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3549" data-relevance="498" data-term="rectangle" data-encoded-term="rectangle" data-term-stats="0	1.7	0.000	3549	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rectangle" onclick="window.location=this.dataset.href" rel="nofollow">rectangle</a>
          </span>
          <span class="term-help" data-term="rectangle"><a href="/pebble#define=rectangle" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1397" data-relevance="497" data-term="seashells" data-encoded-term="seashells" data-term-stats="0	1.8	0.000	1397	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/seashells" onclick="window.location=this.dataset.href" rel="nofollow">seashells</a>
          </span>
          <span class="term-help" data-term="seashells"><a href="/pebble#define=seashells" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3144" data-relevance="496" data-term="clump" data-encoded-term="clump" data-term-stats="0	1.6	0.000	3144	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/clump" onclick="window.location=this.dataset.href" rel="nofollow">clump</a>
          </span>
          <span class="term-help" data-term="clump"><a href="/pebble#define=clump" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2990" data-relevance="495" data-term="driftwood" data-encoded-term="driftwood" data-term-stats="0	1.6	0.000	2990	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/driftwood" onclick="window.location=this.dataset.href" rel="nofollow">driftwood</a>
          </span>
          <span class="term-help" data-term="driftwood"><a href="/pebble#define=driftwood" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="205" data-relevance="494" data-term="dimpled" data-encoded-term="dimpled" data-term-stats="0	1.6	0.000	205	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dimpled" onclick="window.location=this.dataset.href" rel="nofollow">dimpled</a>
          </span>
          <span class="term-help" data-term="dimpled"><a href="/pebble#define=dimpled" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="16956" data-relevance="493" data-term="crushed" data-encoded-term="crushed" data-term-stats="undefined	0.0	0.000	16956	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crushed" onclick="window.location=this.dataset.href" rel="nofollow">crushed</a>
          </span>
          <span class="term-help" data-term="crushed"><a href="/pebble#define=crushed" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1283" data-relevance="492" data-term="powdery" data-encoded-term="powdery" data-term-stats="0	1.6	0.000	1283	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/powdery" onclick="window.location=this.dataset.href" rel="nofollow">powdery</a>
          </span>
          <span class="term-help" data-term="powdery"><a href="/pebble#define=powdery" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="408" data-relevance="491" data-term="trowel" data-encoded-term="trowel" data-term-stats="0	1.6	0.000	408	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/trowel" onclick="window.location=this.dataset.href" rel="nofollow">trowel</a>
          </span>
          <span class="term-help" data-term="trowel"><a href="/pebble#define=trowel" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="89267" data-relevance="490" data-term="clay" data-encoded-term="clay" data-term-stats="undefined	0.0	0.000	89267	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/clay" onclick="window.location=this.dataset.href" rel="nofollow">clay</a>
          </span>
          <span class="term-help" data-term="clay"><a href="/pebble#define=clay" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2628" data-relevance="489" data-term="marbles" data-encoded-term="marbles" data-term-stats="0	1.7	0.000	2628	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/marbles" onclick="window.location=this.dataset.href" rel="nofollow">marbles</a>
          </span>
          <span class="term-help" data-term="marbles"><a href="/pebble#define=marbles" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1301" data-relevance="488" data-term="nothingness" data-encoded-term="nothingness" data-term-stats="0	1.6	0.000	1301	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nothingness" onclick="window.location=this.dataset.href" rel="nofollow">nothingness</a>
          </span>
          <span class="term-help" data-term="nothingness"><a href="/pebble#define=nothingness" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1040" data-relevance="487" data-term="indentation" data-encoded-term="indentation" data-term-stats="0	1.5	0.000	1040	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/indentation" onclick="window.location=this.dataset.href" rel="nofollow">indentation</a>
          </span>
          <span class="term-help" data-term="indentation"><a href="/pebble#define=indentation" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2038" data-relevance="486" data-term="oval shaped" data-encoded-term="oval%20shaped" data-term-stats="0	1.5	0.000	2038	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oval-shaped" onclick="window.location=this.dataset.href" rel="nofollow">oval shaped</a>
          </span>
          <span class="term-help" data-term="oval shaped"><a href="/pebble#define=oval shaped" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2805" data-relevance="485" data-term="shards" data-encoded-term="shards" data-term-stats="0	1.6	0.000	2805	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/shards" onclick="window.location=this.dataset.href" rel="nofollow">shards</a>
          </span>
          <span class="term-help" data-term="shards"><a href="/pebble#define=shards" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="8678" data-relevance="484" data-term="domino" data-encoded-term="domino" data-term-stats="0	1.5	0.000	8678	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/domino" onclick="window.location=this.dataset.href" rel="nofollow">domino</a>
          </span>
          <span class="term-help" data-term="domino"><a href="/pebble#define=domino" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="284" data-relevance="483" data-term="turd" data-encoded-term="turd" data-term-stats="0	1.5	0.000	284	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/turd" onclick="window.location=this.dataset.href" rel="nofollow">turd</a>
          </span>
          <span class="term-help" data-term="turd"><a href="/pebble#define=turd" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="11101" data-relevance="482" data-term="tiles" data-encoded-term="tiles" data-term-stats="0	1.5	0.000	11101	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tiles" onclick="window.location=this.dataset.href" rel="nofollow">tiles</a>
          </span>
          <span class="term-help" data-term="tiles"><a href="/pebble#define=tiles" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1953" data-relevance="481" data-term="droplets" data-encoded-term="droplets" data-term-stats="0	1.5	0.000	1953	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/droplets" onclick="window.location=this.dataset.href" rel="nofollow">droplets</a>
          </span>
          <span class="term-help" data-term="droplets"><a href="/pebble#define=droplets" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5661" data-relevance="480" data-term="oblong" data-encoded-term="oblong" data-term-stats="0	1.5	0.000	5661	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oblong" onclick="window.location=this.dataset.href" rel="nofollow">oblong</a>
          </span>
          <span class="term-help" data-term="oblong"><a href="/pebble#define=oblong" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="65905" data-relevance="479" data-term="rocky" data-encoded-term="rocky" data-term-stats="1	0.7	0.000	65905	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rocky" onclick="window.location=this.dataset.href" rel="nofollow">rocky</a>
          </span>
          <span class="term-help" data-term="rocky"><a href="/pebble#define=rocky" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="48061" data-relevance="478" data-term="stones" data-encoded-term="stones" data-term-stats="1	1.6	0.000	48061	ol|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stones" onclick="window.location=this.dataset.href" rel="nofollow">stones</a>
          </span>
          <span class="term-help" data-term="stones"><a href="/pebble#define=stones" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="664" data-relevance="477" data-term="fingernail" data-encoded-term="fingernail" data-term-stats="0	1.5	0.000	664	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/fingernail" onclick="window.location=this.dataset.href" rel="nofollow">fingernail</a>
          </span>
          <span class="term-help" data-term="fingernail"><a href="/pebble#define=fingernail" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="476" data-term="rebble" data-encoded-term="rebble" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rebble" onclick="window.location=this.dataset.href" rel="nofollow">rebble</a>
          </span>
          <span class="term-help" data-term="rebble"><a href="/pebble#define=rebble" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="69618" data-relevance="475" data-term="sand" data-encoded-term="sand" data-term-stats="1	0.8	0.000	69618	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sand" onclick="window.location=this.dataset.href" rel="nofollow">sand</a>
          </span>
          <span class="term-help" data-term="sand"><a href="/pebble#define=sand" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4261" data-relevance="474" data-term="ice cubes" data-encoded-term="ice%20cubes" data-term-stats="0	1.4	0.000	4261	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ice-cubes" onclick="window.location=this.dataset.href" rel="nofollow">ice cubes</a>
          </span>
          <span class="term-help" data-term="ice cubes"><a href="/pebble#define=ice cubes" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="16563" data-relevance="473" data-term="erosion" data-encoded-term="erosion" data-term-stats="1	1.4	0.000	16563	wiki,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/erosion" onclick="window.location=this.dataset.href" rel="nofollow">erosion</a>
          </span>
          <span class="term-help" data-term="erosion"><a href="/pebble#define=erosion" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3492" data-relevance="472" data-term="meteorite" data-encoded-term="meteorite" data-term-stats="0	1.4	0.000	3492	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/meteorite" onclick="window.location=this.dataset.href" rel="nofollow">meteorite</a>
          </span>
          <span class="term-help" data-term="meteorite"><a href="/pebble#define=meteorite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9964" data-relevance="471" data-term="petals" data-encoded-term="petals" data-term-stats="0	1.4	0.000	9964	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/petals" onclick="window.location=this.dataset.href" rel="nofollow">petals</a>
          </span>
          <span class="term-help" data-term="petals"><a href="/pebble#define=petals" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1655" data-relevance="470" data-term="shard" data-encoded-term="shard" data-term-stats="0	1.0	0.000	1655	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/shard" onclick="window.location=this.dataset.href" rel="nofollow">shard</a>
          </span>
          <span class="term-help" data-term="shard"><a href="/pebble#define=shard" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="194506" data-relevance="469" data-term="surface" data-encoded-term="surface" data-term-stats="0	1.4	0.000	194506	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/surface" onclick="window.location=this.dataset.href" rel="nofollow">surface</a>
          </span>
          <span class="term-help" data-term="surface"><a href="/pebble#define=surface" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="710585" data-relevance="468" data-term="great" data-encoded-term="great" data-term-stats="undefined	0.0	0.000	710585	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/great" onclick="window.location=this.dataset.href" rel="nofollow">great</a>
          </span>
          <span class="term-help" data-term="great"><a href="/pebble#define=great" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4202" data-relevance="467" data-term="sandal" data-encoded-term="sandal" data-term-stats="0	1.3	0.000	4202	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sandal" onclick="window.location=this.dataset.href" rel="nofollow">sandal</a>
          </span>
          <span class="term-help" data-term="sandal"><a href="/pebble#define=sandal" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="106343" data-relevance="466" data-term="habitat" data-encoded-term="habitat" data-term-stats="1	1.4	0.000	106343	wiki,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/habitat" onclick="window.location=this.dataset.href" rel="nofollow">habitat</a>
          </span>
          <span class="term-help" data-term="habitat"><a href="/pebble#define=habitat" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="13220" data-relevance="465" data-term="humidity" data-encoded-term="humidity" data-term-stats="undefined	0.0	0.000	13220	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/humidity" onclick="window.location=this.dataset.href" rel="nofollow">humidity</a>
          </span>
          <span class="term-help" data-term="humidity"><a href="/pebble#define=humidity" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="464" data-term="water" data-encoded-term="water" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/water" onclick="window.location=this.dataset.href" rel="nofollow">water</a>
          </span>
          <span class="term-help" data-term="water"><a href="/pebble#define=water" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="463" data-term="arc" data-encoded-term="arc" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/arc" onclick="window.location=this.dataset.href" rel="nofollow">arc</a>
          </span>
          <span class="term-help" data-term="arc"><a href="/pebble#define=arc" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9265" data-relevance="462" data-term="slab" data-encoded-term="slab" data-term-stats="0	1.3	0.000	9265	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/slab" onclick="window.location=this.dataset.href" rel="nofollow">slab</a>
          </span>
          <span class="term-help" data-term="slab"><a href="/pebble#define=slab" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="13549" data-relevance="461" data-term="cube" data-encoded-term="cube" data-term-stats="0	1.5	0.000	13549	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cube" onclick="window.location=this.dataset.href" rel="nofollow">cube</a>
          </span>
          <span class="term-help" data-term="cube"><a href="/pebble#define=cube" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3462" data-relevance="460" data-term="jagged" data-encoded-term="jagged" data-term-stats="0	1.3	0.000	3462	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/jagged" onclick="window.location=this.dataset.href" rel="nofollow">jagged</a>
          </span>
          <span class="term-help" data-term="jagged"><a href="/pebble#define=jagged" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5094" data-relevance="459" data-term="concave" data-encoded-term="concave" data-term-stats="0	1.3	0.000	5094	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/concave" onclick="window.location=this.dataset.href" rel="nofollow">concave</a>
          </span>
          <span class="term-help" data-term="concave"><a href="/pebble#define=concave" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="458" data-term="humidifier" data-encoded-term="humidifier" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/humidifier" onclick="window.location=this.dataset.href" rel="nofollow">humidifier</a>
          </span>
          <span class="term-help" data-term="humidifier"><a href="/pebble#define=humidifier" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="65" data-relevance="457" data-term="teeny tiny" data-encoded-term="teeny%20tiny" data-term-stats="0	1.3	0.000	65	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/teeny-tiny" onclick="window.location=this.dataset.href" rel="nofollow">teeny tiny</a>
          </span>
          <span class="term-help" data-term="teeny tiny"><a href="/pebble#define=teeny tiny" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="23377" data-relevance="456" data-term="dirt" data-encoded-term="dirt" data-term-stats="0	1.4	0.000	23377	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dirt" onclick="window.location=this.dataset.href" rel="nofollow">dirt</a>
          </span>
          <span class="term-help" data-term="dirt"><a href="/pebble#define=dirt" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="8284" data-relevance="455" data-term="sponge" data-encoded-term="sponge" data-term-stats="0	1.3	0.000	8284	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sponge" onclick="window.location=this.dataset.href" rel="nofollow">sponge</a>
          </span>
          <span class="term-help" data-term="sponge"><a href="/pebble#define=sponge" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="38059" data-relevance="454" data-term="moss" data-encoded-term="moss" data-term-stats="0	1.3	0.000	38059	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/moss" onclick="window.location=this.dataset.href" rel="nofollow">moss</a>
          </span>
          <span class="term-help" data-term="moss"><a href="/pebble#define=moss" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5494" data-relevance="453" data-term="silvery" data-encoded-term="silvery" data-term-stats="0	1.4	0.000	5494	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/silvery" onclick="window.location=this.dataset.href" rel="nofollow">silvery</a>
          </span>
          <span class="term-help" data-term="silvery"><a href="/pebble#define=silvery" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="10365" data-relevance="452" data-term="tile" data-encoded-term="tile" data-term-stats="0	1.3	0.000	10365	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tile" onclick="window.location=this.dataset.href" rel="nofollow">tile</a>
          </span>
          <span class="term-help" data-term="tile"><a href="/pebble#define=tile" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="25915" data-relevance="451" data-term="rectangular" data-encoded-term="rectangular" data-term-stats="0	1.3	0.000	25915	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rectangular" onclick="window.location=this.dataset.href" rel="nofollow">rectangular</a>
          </span>
          <span class="term-help" data-term="rectangular"><a href="/pebble#define=rectangular" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="479" data-relevance="450" data-term="dust particles" data-encoded-term="dust%20particles" data-term-stats="0	1.2	0.000	479	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dust-particles" onclick="window.location=this.dataset.href" rel="nofollow">dust particles</a>
          </span>
          <span class="term-help" data-term="dust particles"><a href="/pebble#define=dust particles" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="449" data-term="plaster" data-encoded-term="plaster" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/plaster" onclick="window.location=this.dataset.href" rel="nofollow">plaster</a>
          </span>
          <span class="term-help" data-term="plaster"><a href="/pebble#define=plaster" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3468" data-relevance="448" data-term="depressions" data-encoded-term="depressions" data-term-stats="0	1.2	0.000	3468	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/depressions" onclick="window.location=this.dataset.href" rel="nofollow">depressions</a>
          </span>
          <span class="term-help" data-term="depressions"><a href="/pebble#define=depressions" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="422" data-relevance="447" data-term="pavers" data-encoded-term="pavers" data-term-stats="0	1.2	0.000	422	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pavers" onclick="window.location=this.dataset.href" rel="nofollow">pavers</a>
          </span>
          <span class="term-help" data-term="pavers"><a href="/pebble#define=pavers" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2041" data-relevance="446" data-term="frisbee" data-encoded-term="frisbee" data-term-stats="0	1.2	0.000	2041	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/frisbee" onclick="window.location=this.dataset.href" rel="nofollow">frisbee</a>
          </span>
          <span class="term-help" data-term="frisbee"><a href="/pebble#define=frisbee" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="16973" data-relevance="445" data-term="fragment" data-encoded-term="fragment" data-term-stats="0	1.4	0.000	16973	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/fragment" onclick="window.location=this.dataset.href" rel="nofollow">fragment</a>
          </span>
          <span class="term-help" data-term="fragment"><a href="/pebble#define=fragment" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="316" data-relevance="444" data-term="bread crumbs" data-encoded-term="bread%20crumbs" data-term-stats="0	1.2	0.000	316	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bread-crumbs" onclick="window.location=this.dataset.href" rel="nofollow">bread crumbs</a>
          </span>
          <span class="term-help" data-term="bread crumbs"><a href="/pebble#define=bread crumbs" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="668" data-relevance="443" data-term="spyglass" data-encoded-term="spyglass" data-term-stats="1	0.5	0.000	668	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spyglass" onclick="window.location=this.dataset.href" rel="nofollow">spyglass</a>
          </span>
          <span class="term-help" data-term="spyglass"><a href="/pebble#define=spyglass" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="442" data-term="monterey" data-encoded-term="monterey" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/monterey" onclick="window.location=this.dataset.href" rel="nofollow">monterey</a>
          </span>
          <span class="term-help" data-term="monterey"><a href="/pebble#define=monterey" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="441" data-term="swift" data-encoded-term="swift" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/swift" onclick="window.location=this.dataset.href" rel="nofollow">swift</a>
          </span>
          <span class="term-help" data-term="swift"><a href="/pebble#define=swift" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="440" data-term="carmel" data-encoded-term="carmel" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/carmel" onclick="window.location=this.dataset.href" rel="nofollow">carmel</a>
          </span>
          <span class="term-help" data-term="carmel"><a href="/pebble#define=carmel" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1189" data-relevance="439" data-term="shingle beach" data-encoded-term="shingle%20beach" data-term-stats="1	1.2	0.000	1189	wiki,swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/shingle-beach" onclick="window.location=this.dataset.href" rel="nofollow">shingle beach</a>
          </span>
          <span class="term-help" data-term="shingle beach"><a href="/pebble#define=shingle beach" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2164" data-relevance="438" data-term="crevices" data-encoded-term="crevices" data-term-stats="0	1.2	0.000	2164	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crevices" onclick="window.location=this.dataset.href" rel="nofollow">crevices</a>
          </span>
          <span class="term-help" data-term="crevices"><a href="/pebble#define=crevices" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="66642" data-relevance="437" data-term="crystal" data-encoded-term="crystal" data-term-stats="0	1.2	0.000	66642	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crystal" onclick="window.location=this.dataset.href" rel="nofollow">crystal</a>
          </span>
          <span class="term-help" data-term="crystal"><a href="/pebble#define=crystal" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1197" data-relevance="436" data-term="dinky" data-encoded-term="dinky" data-term-stats="0	1.1	0.000	1197	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dinky" onclick="window.location=this.dataset.href" rel="nofollow">dinky</a>
          </span>
          <span class="term-help" data-term="dinky"><a href="/pebble#define=dinky" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="29854" data-relevance="435" data-term="mud" data-encoded-term="mud" data-term-stats="0	1.1	0.000	29854	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/mud" onclick="window.location=this.dataset.href" rel="nofollow">mud</a>
          </span>
          <span class="term-help" data-term="mud"><a href="/pebble#define=mud" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="661" data-relevance="434" data-term="blobs" data-encoded-term="blobs" data-term-stats="0	1.2	0.000	661	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/blobs" onclick="window.location=this.dataset.href" rel="nofollow">blobs</a>
          </span>
          <span class="term-help" data-term="blobs"><a href="/pebble#define=blobs" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2198" data-relevance="433" data-term="quicksand" data-encoded-term="quicksand" data-term-stats="0	1.1	0.000	2198	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/quicksand" onclick="window.location=this.dataset.href" rel="nofollow">quicksand</a>
          </span>
          <span class="term-help" data-term="quicksand"><a href="/pebble#define=quicksand" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="432" data-term="concrete" data-encoded-term="concrete" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/concrete" onclick="window.location=this.dataset.href" rel="nofollow">concrete</a>
          </span>
          <span class="term-help" data-term="concrete"><a href="/pebble#define=concrete" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="431" data-term="lay" data-encoded-term="lay" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lay" onclick="window.location=this.dataset.href" rel="nofollow">lay</a>
          </span>
          <span class="term-help" data-term="lay"><a href="/pebble#define=lay" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="430" data-term="spanish" data-encoded-term="spanish" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spanish" onclick="window.location=this.dataset.href" rel="nofollow">spanish</a>
          </span>
          <span class="term-help" data-term="spanish"><a href="/pebble#define=spanish" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="429" data-term="perlite" data-encoded-term="perlite" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/perlite" onclick="window.location=this.dataset.href" rel="nofollow">perlite</a>
          </span>
          <span class="term-help" data-term="perlite"><a href="/pebble#define=perlite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="428" data-term="flashbang" data-encoded-term="flashbang" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flashbang" onclick="window.location=this.dataset.href" rel="nofollow">flashbang</a>
          </span>
          <span class="term-help" data-term="flashbang"><a href="/pebble#define=flashbang" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="427" data-term="gizmo" data-encoded-term="gizmo" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gizmo" onclick="window.location=this.dataset.href" rel="nofollow">gizmo</a>
          </span>
          <span class="term-help" data-term="gizmo"><a href="/pebble#define=gizmo" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="426" data-term="eastern" data-encoded-term="eastern" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/eastern" onclick="window.location=this.dataset.href" rel="nofollow">eastern</a>
          </span>
          <span class="term-help" data-term="eastern"><a href="/pebble#define=eastern" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="425" data-term="phalanx" data-encoded-term="phalanx" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/phalanx" onclick="window.location=this.dataset.href" rel="nofollow">phalanx</a>
          </span>
          <span class="term-help" data-term="phalanx"><a href="/pebble#define=phalanx" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="10373" data-relevance="424" data-term="crystals" data-encoded-term="crystals" data-term-stats="0	1.1	0.000	10373	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crystals" onclick="window.location=this.dataset.href" rel="nofollow">crystals</a>
          </span>
          <span class="term-help" data-term="crystals"><a href="/pebble#define=crystals" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="12639" data-relevance="423" data-term="bricks" data-encoded-term="bricks" data-term-stats="0	1.4	0.000	12639	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bricks" onclick="window.location=this.dataset.href" rel="nofollow">bricks</a>
          </span>
          <span class="term-help" data-term="bricks"><a href="/pebble#define=bricks" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="18443" data-relevance="422" data-term="particles" data-encoded-term="particles" data-term-stats="0	1.1	0.000	18443	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/particles" onclick="window.location=this.dataset.href" rel="nofollow">particles</a>
          </span>
          <span class="term-help" data-term="particles"><a href="/pebble#define=particles" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="37571" data-relevance="421" data-term="marble" data-encoded-term="marble" data-term-stats="1	0.7	0.000	37571	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/marble" onclick="window.location=this.dataset.href" rel="nofollow">marble</a>
          </span>
          <span class="term-help" data-term="marble"><a href="/pebble#define=marble" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="17052" data-relevance="420" data-term="cubic" data-encoded-term="cubic" data-term-stats="0	1.1	0.000	17052	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cubic" onclick="window.location=this.dataset.href" rel="nofollow">cubic</a>
          </span>
          <span class="term-help" data-term="cubic"><a href="/pebble#define=cubic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="225" data-relevance="419" data-term="gurgling" data-encoded-term="gurgling" data-term-stats="0	1.1	0.000	225	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gurgling" onclick="window.location=this.dataset.href" rel="nofollow">gurgling</a>
          </span>
          <span class="term-help" data-term="gurgling"><a href="/pebble#define=gurgling" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="25999" data-relevance="418" data-term="sandstone" data-encoded-term="sandstone" data-term-stats="1	1.0	0.000	25999	cn5|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sandstone" onclick="window.location=this.dataset.href" rel="nofollow">sandstone</a>
          </span>
          <span class="term-help" data-term="sandstone"><a href="/pebble#define=sandstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="575" data-relevance="417" data-term="sandpaper" data-encoded-term="sandpaper" data-term-stats="0	1.1	0.000	575	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sandpaper" onclick="window.location=this.dataset.href" rel="nofollow">sandpaper</a>
          </span>
          <span class="term-help" data-term="sandpaper"><a href="/pebble#define=sandpaper" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2463" data-relevance="416" data-term="flake" data-encoded-term="flake" data-term-stats="0	1.4	0.000	2463	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flake" onclick="window.location=this.dataset.href" rel="nofollow">flake</a>
          </span>
          <span class="term-help" data-term="flake"><a href="/pebble#define=flake" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="8276" data-relevance="415" data-term="pea" data-encoded-term="pea" data-term-stats="1	0.7	0.000	8276	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pea" onclick="window.location=this.dataset.href" rel="nofollow">pea</a>
          </span>
          <span class="term-help" data-term="pea"><a href="/pebble#define=pea" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2165" data-relevance="414" data-term="tree trunk" data-encoded-term="tree%20trunk" data-term-stats="0	1.1	0.000	2165	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tree-trunk" onclick="window.location=this.dataset.href" rel="nofollow">tree trunk</a>
          </span>
          <span class="term-help" data-term="tree trunk"><a href="/pebble#define=tree trunk" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="61319" data-relevance="413" data-term="sandy" data-encoded-term="sandy" data-term-stats="1	0.8	0.000	61319	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sandy" onclick="window.location=this.dataset.href" rel="nofollow">sandy</a>
          </span>
          <span class="term-help" data-term="sandy"><a href="/pebble#define=sandy" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2966" data-relevance="412" data-term="saucer" data-encoded-term="saucer" data-term-stats="0	1.1	0.000	2966	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/saucer" onclick="window.location=this.dataset.href" rel="nofollow">saucer</a>
          </span>
          <span class="term-help" data-term="saucer"><a href="/pebble#define=saucer" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2508" data-relevance="411" data-term="nugget" data-encoded-term="nugget" data-term-stats="1	0.5	0.000	2508	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nugget" onclick="window.location=this.dataset.href" rel="nofollow">nugget</a>
          </span>
          <span class="term-help" data-term="nugget"><a href="/pebble#define=nugget" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2861" data-relevance="410" data-term="fleck" data-encoded-term="fleck" data-term-stats="1	0.4	0.000	2861	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/fleck" onclick="window.location=this.dataset.href" rel="nofollow">fleck</a>
          </span>
          <span class="term-help" data-term="fleck"><a href="/pebble#define=fleck" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="59200" data-relevance="409" data-term="soil" data-encoded-term="soil" data-term-stats="1	0.1	0.000	59200	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/soil" onclick="window.location=this.dataset.href" rel="nofollow">soil</a>
          </span>
          <span class="term-help" data-term="soil"><a href="/pebble#define=soil" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1114" data-relevance="408" data-term="pothole" data-encoded-term="pothole" data-term-stats="0	1.1	0.000	1114	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pothole" onclick="window.location=this.dataset.href" rel="nofollow">pothole</a>
          </span>
          <span class="term-help" data-term="pothole"><a href="/pebble#define=pothole" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="335" data-relevance="407" data-term="glass jar" data-encoded-term="glass%20jar" data-term-stats="0	1.0	0.000	335	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/glass-jar" onclick="window.location=this.dataset.href" rel="nofollow">glass jar</a>
          </span>
          <span class="term-help" data-term="glass jar"><a href="/pebble#define=glass jar" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2322" data-relevance="406" data-term="hourglass" data-encoded-term="hourglass" data-term-stats="0	1.0	0.000	2322	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hourglass" onclick="window.location=this.dataset.href" rel="nofollow">hourglass</a>
          </span>
          <span class="term-help" data-term="hourglass"><a href="/pebble#define=hourglass" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3572" data-relevance="405" data-term="petal" data-encoded-term="petal" data-term-stats="0	1.0	0.000	3572	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/petal" onclick="window.location=this.dataset.href" rel="nofollow">petal</a>
          </span>
          <span class="term-help" data-term="petal"><a href="/pebble#define=petal" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="19063" data-relevance="404" data-term="gc" data-encoded-term="gc" data-term-stats="1	1.0	0.000	19063	w2v|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gc" onclick="window.location=this.dataset.href" rel="nofollow">gc</a>
          </span>
          <span class="term-help" data-term="gc"><a href="/pebble#define=gc" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="35362" data-relevance="403" data-term="limestone" data-encoded-term="limestone" data-term-stats="1	0.9	0.000	35362	cn5|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/limestone" onclick="window.location=this.dataset.href" rel="nofollow">limestone</a>
          </span>
          <span class="term-help" data-term="limestone"><a href="/pebble#define=limestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3317" data-relevance="402" data-term="slipper" data-encoded-term="slipper" data-term-stats="1	0.8	0.000	3317	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/slipper" onclick="window.location=this.dataset.href" rel="nofollow">slipper</a>
          </span>
          <span class="term-help" data-term="slipper"><a href="/pebble#define=slipper" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1677" data-relevance="401" data-term="twig" data-encoded-term="twig" data-term-stats="1	0.6	0.000	1677	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/twig" onclick="window.location=this.dataset.href" rel="nofollow">twig</a>
          </span>
          <span class="term-help" data-term="twig"><a href="/pebble#define=twig" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2126" data-relevance="400" data-term="crevice" data-encoded-term="crevice" data-term-stats="1	0.8	0.000	2126	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crevice" onclick="window.location=this.dataset.href" rel="nofollow">crevice</a>
          </span>
          <span class="term-help" data-term="crevice"><a href="/pebble#define=crevice" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1272" data-relevance="399" data-term="pinehurst" data-encoded-term="pinehurst" data-term-stats="1	0.5	0.000	1272	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pinehurst" onclick="window.location=this.dataset.href" rel="nofollow">pinehurst</a>
          </span>
          <span class="term-help" data-term="pinehurst"><a href="/pebble#define=pinehurst" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="24850" data-relevance="398" data-term="augusta" data-encoded-term="augusta" data-term-stats="1	0.4	0.000	24850	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/augusta" onclick="window.location=this.dataset.href" rel="nofollow">augusta</a>
          </span>
          <span class="term-help" data-term="augusta"><a href="/pebble#define=augusta" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9265" data-relevance="397" data-term="quartz" data-encoded-term="quartz" data-term-stats="1	0.4	0.000	9265	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/quartz" onclick="window.location=this.dataset.href" rel="nofollow">quartz</a>
          </span>
          <span class="term-help" data-term="quartz"><a href="/pebble#define=quartz" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1840" data-relevance="396" data-term="stonemason" data-encoded-term="stonemason" data-term-stats="1	0.7	0.000	1840	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonemason" onclick="window.location=this.dataset.href" rel="nofollow">stonemason</a>
          </span>
          <span class="term-help" data-term="stonemason"><a href="/pebble#define=stonemason" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="663" data-relevance="395" data-term="soapstone" data-encoded-term="soapstone" data-term-stats="1	0.7	0.000	663	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/soapstone" onclick="window.location=this.dataset.href" rel="nofollow">soapstone</a>
          </span>
          <span class="term-help" data-term="soapstone"><a href="/pebble#define=soapstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1697" data-relevance="394" data-term="ripples" data-encoded-term="ripples" data-term-stats="1	0.7	0.000	1697	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ripples" onclick="window.location=this.dataset.href" rel="nofollow">ripples</a>
          </span>
          <span class="term-help" data-term="ripples"><a href="/pebble#define=ripples" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3635" data-relevance="393" data-term="ashlar" data-encoded-term="ashlar" data-term-stats="1	0.7	0.000	3635	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ashlar" onclick="window.location=this.dataset.href" rel="nofollow">ashlar</a>
          </span>
          <span class="term-help" data-term="ashlar"><a href="/pebble#define=ashlar" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="723" data-relevance="392" data-term="runestone" data-encoded-term="runestone" data-term-stats="1	0.7	0.000	723	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/runestone" onclick="window.location=this.dataset.href" rel="nofollow">runestone</a>
          </span>
          <span class="term-help" data-term="runestone"><a href="/pebble#define=runestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2988" data-relevance="391" data-term="stonework" data-encoded-term="stonework" data-term-stats="1	0.7	0.000	2988	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonework" onclick="window.location=this.dataset.href" rel="nofollow">stonework</a>
          </span>
          <span class="term-help" data-term="stonework"><a href="/pebble#define=stonework" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="953" data-relevance="390" data-term="menhir" data-encoded-term="menhir" data-term-stats="1	0.7	0.000	953	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/menhir" onclick="window.location=this.dataset.href" rel="nofollow">menhir</a>
          </span>
          <span class="term-help" data-term="menhir"><a href="/pebble#define=menhir" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2393" data-relevance="389" data-term="puddle" data-encoded-term="puddle" data-term-stats="1	0.7	0.000	2393	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/puddle" onclick="window.location=this.dataset.href" rel="nofollow">puddle</a>
          </span>
          <span class="term-help" data-term="puddle"><a href="/pebble#define=puddle" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="237" data-relevance="388" data-term="lodestone" data-encoded-term="lodestone" data-term-stats="1	0.7	0.000	237	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lodestone" onclick="window.location=this.dataset.href" rel="nofollow">lodestone</a>
          </span>
          <span class="term-help" data-term="lodestone"><a href="/pebble#define=lodestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1583" data-relevance="387" data-term="fieldstone" data-encoded-term="fieldstone" data-term-stats="1	0.7	0.000	1583	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/fieldstone" onclick="window.location=this.dataset.href" rel="nofollow">fieldstone</a>
          </span>
          <span class="term-help" data-term="fieldstone"><a href="/pebble#define=fieldstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="7259" data-relevance="386" data-term="sedimentary" data-encoded-term="sedimentary" data-term-stats="1	0.7	0.000	7259	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sedimentary" onclick="window.location=this.dataset.href" rel="nofollow">sedimentary</a>
          </span>
          <span class="term-help" data-term="sedimentary"><a href="/pebble#define=sedimentary" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2136" data-relevance="385" data-term="lithic" data-encoded-term="lithic" data-term-stats="1	0.7	0.000	2136	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lithic" onclick="window.location=this.dataset.href" rel="nofollow">lithic</a>
          </span>
          <span class="term-help" data-term="lithic"><a href="/pebble#define=lithic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1127" data-relevance="384" data-term="pail" data-encoded-term="pail" data-term-stats="1	0.7	0.000	1127	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pail" onclick="window.location=this.dataset.href" rel="nofollow">pail</a>
          </span>
          <span class="term-help" data-term="pail"><a href="/pebble#define=pail" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2371" data-relevance="383" data-term="whetstone" data-encoded-term="whetstone" data-term-stats="1	0.7	0.000	2371	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/whetstone" onclick="window.location=this.dataset.href" rel="nofollow">whetstone</a>
          </span>
          <span class="term-help" data-term="whetstone"><a href="/pebble#define=whetstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="915" data-relevance="382" data-term="stoneware" data-encoded-term="stoneware" data-term-stats="1	0.7	0.000	915	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stoneware" onclick="window.location=this.dataset.href" rel="nofollow">stoneware</a>
          </span>
          <span class="term-help" data-term="stoneware"><a href="/pebble#define=stoneware" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2042" data-relevance="381" data-term="granules" data-encoded-term="granules" data-term-stats="1	0.7	0.000	2042	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/granules" onclick="window.location=this.dataset.href" rel="nofollow">granules</a>
          </span>
          <span class="term-help" data-term="granules"><a href="/pebble#define=granules" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="492" data-relevance="380" data-term="diorite" data-encoded-term="diorite" data-term-stats="1	0.7	0.000	492	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/diorite" onclick="window.location=this.dataset.href" rel="nofollow">diorite</a>
          </span>
          <span class="term-help" data-term="diorite"><a href="/pebble#define=diorite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1053" data-relevance="379" data-term="krautrock" data-encoded-term="krautrock" data-term-stats="1	0.7	0.000	1053	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/krautrock" onclick="window.location=this.dataset.href" rel="nofollow">krautrock</a>
          </span>
          <span class="term-help" data-term="krautrock"><a href="/pebble#define=krautrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1050" data-relevance="378" data-term="grindstone" data-encoded-term="grindstone" data-term-stats="1	0.7	0.000	1050	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/grindstone" onclick="window.location=this.dataset.href" rel="nofollow">grindstone</a>
          </span>
          <span class="term-help" data-term="grindstone"><a href="/pebble#define=grindstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="6120" data-relevance="377" data-term="bedrock" data-encoded-term="bedrock" data-term-stats="1	0.7	0.000	6120	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bedrock" onclick="window.location=this.dataset.href" rel="nofollow">bedrock</a>
          </span>
          <span class="term-help" data-term="bedrock"><a href="/pebble#define=bedrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="82" data-relevance="376" data-term="petrifaction" data-encoded-term="petrifaction" data-term-stats="1	0.7	0.000	82	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/petrifaction" onclick="window.location=this.dataset.href" rel="nofollow">petrifaction</a>
          </span>
          <span class="term-help" data-term="petrifaction"><a href="/pebble#define=petrifaction" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2961" data-relevance="375" data-term="speck" data-encoded-term="speck" data-term-stats="1	0.7	0.000	2961	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/speck" onclick="window.location=this.dataset.href" rel="nofollow">speck</a>
          </span>
          <span class="term-help" data-term="speck"><a href="/pebble#define=speck" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1136" data-relevance="374" data-term="andesite" data-encoded-term="andesite" data-term-stats="1	0.7	0.000	1136	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/andesite" onclick="window.location=this.dataset.href" rel="nofollow">andesite</a>
          </span>
          <span class="term-help" data-term="andesite"><a href="/pebble#define=andesite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5608" data-relevance="373" data-term="basalt" data-encoded-term="basalt" data-term-stats="1	0.7	0.000	5608	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/basalt" onclick="window.location=this.dataset.href" rel="nofollow">basalt</a>
          </span>
          <span class="term-help" data-term="basalt"><a href="/pebble#define=basalt" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1095" data-relevance="372" data-term="moonstone" data-encoded-term="moonstone" data-term-stats="1	0.7	0.000	1095	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/moonstone" onclick="window.location=this.dataset.href" rel="nofollow">moonstone</a>
          </span>
          <span class="term-help" data-term="moonstone"><a href="/pebble#define=moonstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1768" data-relevance="371" data-term="cobblestone" data-encoded-term="cobblestone" data-term-stats="1	0.7	0.000	1768	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cobblestone" onclick="window.location=this.dataset.href" rel="nofollow">cobblestone</a>
          </span>
          <span class="term-help" data-term="cobblestone"><a href="/pebble#define=cobblestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="40480" data-relevance="370" data-term="logan" data-encoded-term="logan" data-term-stats="1	0.7	0.000	40480	cn5|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/logan" onclick="window.location=this.dataset.href" rel="nofollow">logan</a>
          </span>
          <span class="term-help" data-term="logan"><a href="/pebble#define=logan" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3158" data-relevance="369" data-term="suffragist" data-encoded-term="suffragist" data-term-stats="1	0.7	0.000	3158	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/suffragist" onclick="window.location=this.dataset.href" rel="nofollow">suffragist</a>
          </span>
          <span class="term-help" data-term="suffragist"><a href="/pebble#define=suffragist" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1804" data-relevance="368" data-term="snowflake" data-encoded-term="snowflake" data-term-stats="1	0.7	0.000	1804	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/snowflake" onclick="window.location=this.dataset.href" rel="nofollow">snowflake</a>
          </span>
          <span class="term-help" data-term="snowflake"><a href="/pebble#define=snowflake" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1927" data-relevance="367" data-term="gravelly" data-encoded-term="gravelly" data-term-stats="1	0.7	0.000	1927	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gravelly" onclick="window.location=this.dataset.href" rel="nofollow">gravelly</a>
          </span>
          <span class="term-help" data-term="gravelly"><a href="/pebble#define=gravelly" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="19013" data-relevance="366" data-term="shoe" data-encoded-term="shoe" data-term-stats="1	0.7	0.000	19013	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/shoe" onclick="window.location=this.dataset.href" rel="nofollow">shoe</a>
          </span>
          <span class="term-help" data-term="shoe"><a href="/pebble#define=shoe" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2986" data-relevance="365" data-term="monolith" data-encoded-term="monolith" data-term-stats="1	0.7	0.000	2986	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/monolith" onclick="window.location=this.dataset.href" rel="nofollow">monolith</a>
          </span>
          <span class="term-help" data-term="monolith"><a href="/pebble#define=monolith" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="767" data-relevance="364" data-term="flagstone" data-encoded-term="flagstone" data-term-stats="1	0.7	0.000	767	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flagstone" onclick="window.location=this.dataset.href" rel="nofollow">flagstone</a>
          </span>
          <span class="term-help" data-term="flagstone"><a href="/pebble#define=flagstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="168" data-relevance="363" data-term="flinty" data-encoded-term="flinty" data-term-stats="1	0.7	0.000	168	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flinty" onclick="window.location=this.dataset.href" rel="nofollow">flinty</a>
          </span>
          <span class="term-help" data-term="flinty"><a href="/pebble#define=flinty" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3298" data-relevance="362" data-term="crag" data-encoded-term="crag" data-term-stats="1	0.7	0.000	3298	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crag" onclick="window.location=this.dataset.href" rel="nofollow">crag</a>
          </span>
          <span class="term-help" data-term="crag"><a href="/pebble#define=crag" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="919" data-relevance="361" data-term="droplet" data-encoded-term="droplet" data-term-stats="1	0.7	0.000	919	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/droplet" onclick="window.location=this.dataset.href" rel="nofollow">droplet</a>
          </span>
          <span class="term-help" data-term="droplet"><a href="/pebble#define=droplet" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1535" data-relevance="360" data-term="granule" data-encoded-term="granule" data-term-stats="1	0.7	0.000	1535	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/granule" onclick="window.location=this.dataset.href" rel="nofollow">granule</a>
          </span>
          <span class="term-help" data-term="granule"><a href="/pebble#define=granule" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="603" data-relevance="359" data-term="plutonic" data-encoded-term="plutonic" data-term-stats="1	0.7	0.000	603	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/plutonic" onclick="window.location=this.dataset.href" rel="nofollow">plutonic</a>
          </span>
          <span class="term-help" data-term="plutonic"><a href="/pebble#define=plutonic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2314" data-relevance="358" data-term="clumps" data-encoded-term="clumps" data-term-stats="1	0.7	0.000	2314	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/clumps" onclick="window.location=this.dataset.href" rel="nofollow">clumps</a>
          </span>
          <span class="term-help" data-term="clumps"><a href="/pebble#define=clumps" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2092" data-relevance="357" data-term="crumb" data-encoded-term="crumb" data-term-stats="1	0.7	0.000	2092	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crumb" onclick="window.location=this.dataset.href" rel="nofollow">crumb</a>
          </span>
          <span class="term-help" data-term="crumb"><a href="/pebble#define=crumb" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="519" data-relevance="356" data-term="hearthstone" data-encoded-term="hearthstone" data-term-stats="1	0.7	0.000	519	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hearthstone" onclick="window.location=this.dataset.href" rel="nofollow">hearthstone</a>
          </span>
          <span class="term-help" data-term="hearthstone"><a href="/pebble#define=hearthstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="886" data-relevance="355" data-term="rimrock" data-encoded-term="rimrock" data-term-stats="1	0.7	0.000	886	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rimrock" onclick="window.location=this.dataset.href" rel="nofollow">rimrock</a>
          </span>
          <span class="term-help" data-term="rimrock"><a href="/pebble#define=rimrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3482" data-relevance="354" data-term="igneous" data-encoded-term="igneous" data-term-stats="1	0.7	0.000	3482	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/igneous" onclick="window.location=this.dataset.href" rel="nofollow">igneous</a>
          </span>
          <span class="term-help" data-term="igneous"><a href="/pebble#define=igneous" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1624" data-relevance="353" data-term="whitestone" data-encoded-term="whitestone" data-term-stats="1	0.7	0.000	1624	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/whitestone" onclick="window.location=this.dataset.href" rel="nofollow">whitestone</a>
          </span>
          <span class="term-help" data-term="whitestone"><a href="/pebble#define=whitestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="7913" data-relevance="352" data-term="rocker" data-encoded-term="rocker" data-term-stats="1	0.7	0.000	7913	cn5|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rocker" onclick="window.location=this.dataset.href" rel="nofollow">rocker</a>
          </span>
          <span class="term-help" data-term="rocker"><a href="/pebble#define=rocker" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="12530" data-relevance="351" data-term="lava" data-encoded-term="lava" data-term-stats="1	0.7	0.000	12530	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lava" onclick="window.location=this.dataset.href" rel="nofollow">lava</a>
          </span>
          <span class="term-help" data-term="lava"><a href="/pebble#define=lava" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="350" data-term="boulderstone" data-encoded-term="boulderstone" data-term-stats="1	0.7	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/boulderstone" onclick="window.location=this.dataset.href" rel="nofollow">boulderstone</a>
          </span>
          <span class="term-help" data-term="boulderstone"><a href="/pebble#define=boulderstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="581" data-relevance="349" data-term="gritstone" data-encoded-term="gritstone" data-term-stats="1	0.6	0.000	581	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gritstone" onclick="window.location=this.dataset.href" rel="nofollow">gritstone</a>
          </span>
          <span class="term-help" data-term="gritstone"><a href="/pebble#define=gritstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="30090" data-relevance="348" data-term="fragments" data-encoded-term="fragments" data-term-stats="1	0.6	0.000	30090	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/fragments" onclick="window.location=this.dataset.href" rel="nofollow">fragments</a>
          </span>
          <span class="term-help" data-term="fragments"><a href="/pebble#define=fragments" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1400" data-relevance="347" data-term="pyroclastic" data-encoded-term="pyroclastic" data-term-stats="1	0.6	0.000	1400	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pyroclastic" onclick="window.location=this.dataset.href" rel="nofollow">pyroclastic</a>
          </span>
          <span class="term-help" data-term="pyroclastic"><a href="/pebble#define=pyroclastic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="351" data-relevance="346" data-term="claystone" data-encoded-term="claystone" data-term-stats="1	0.6	0.000	351	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/claystone" onclick="window.location=this.dataset.href" rel="nofollow">claystone</a>
          </span>
          <span class="term-help" data-term="claystone"><a href="/pebble#define=claystone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="122" data-relevance="345" data-term="whinstone" data-encoded-term="whinstone" data-term-stats="1	0.6	0.000	122	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/whinstone" onclick="window.location=this.dataset.href" rel="nofollow">whinstone</a>
          </span>
          <span class="term-help" data-term="whinstone"><a href="/pebble#define=whinstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="344" data-term="enrockment" data-encoded-term="enrockment" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/enrockment" onclick="window.location=this.dataset.href" rel="nofollow">enrockment</a>
          </span>
          <span class="term-help" data-term="enrockment"><a href="/pebble#define=enrockment" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1280" data-relevance="343" data-term="freestone" data-encoded-term="freestone" data-term-stats="1	0.6	0.000	1280	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/freestone" onclick="window.location=this.dataset.href" rel="nofollow">freestone</a>
          </span>
          <span class="term-help" data-term="freestone"><a href="/pebble#define=freestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3413" data-relevance="342" data-term="headstone" data-encoded-term="headstone" data-term-stats="1	0.6	0.000	3413	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/headstone" onclick="window.location=this.dataset.href" rel="nofollow">headstone</a>
          </span>
          <span class="term-help" data-term="headstone"><a href="/pebble#define=headstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="341" data-term="stoneless" data-encoded-term="stoneless" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stoneless" onclick="window.location=this.dataset.href" rel="nofollow">stoneless</a>
          </span>
          <span class="term-help" data-term="stoneless"><a href="/pebble#define=stoneless" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="73" data-relevance="340" data-term="chockstone" data-encoded-term="chockstone" data-term-stats="1	0.6	0.000	73	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/chockstone" onclick="window.location=this.dataset.href" rel="nofollow">chockstone</a>
          </span>
          <span class="term-help" data-term="chockstone"><a href="/pebble#define=chockstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="339" data-term="petrean" data-encoded-term="petrean" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/petrean" onclick="window.location=this.dataset.href" rel="nofollow">petrean</a>
          </span>
          <span class="term-help" data-term="petrean"><a href="/pebble#define=petrean" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="338" data-term="stonehearted" data-encoded-term="stonehearted" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonehearted" onclick="window.location=this.dataset.href" rel="nofollow">stonehearted</a>
          </span>
          <span class="term-help" data-term="stonehearted"><a href="/pebble#define=stonehearted" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="38" data-relevance="337" data-term="lapidation" data-encoded-term="lapidation" data-term-stats="1	0.6	0.000	38	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lapidation" onclick="window.location=this.dataset.href" rel="nofollow">lapidation</a>
          </span>
          <span class="term-help" data-term="lapidation"><a href="/pebble#define=lapidation" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="219" data-relevance="336" data-term="rubblestone" data-encoded-term="rubblestone" data-term-stats="1	0.6	0.000	219	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rubblestone" onclick="window.location=this.dataset.href" rel="nofollow">rubblestone</a>
          </span>
          <span class="term-help" data-term="rubblestone"><a href="/pebble#define=rubblestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4292" data-relevance="335" data-term="stratigraphy" data-encoded-term="stratigraphy" data-term-stats="1	0.6	0.000	4292	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stratigraphy" onclick="window.location=this.dataset.href" rel="nofollow">stratigraphy</a>
          </span>
          <span class="term-help" data-term="stratigraphy"><a href="/pebble#define=stratigraphy" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="334" data-term="stonify" data-encoded-term="stonify" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonify" onclick="window.location=this.dataset.href" rel="nofollow">stonify</a>
          </span>
          <span class="term-help" data-term="stonify"><a href="/pebble#define=stonify" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="333" data-term="stonen" data-encoded-term="stonen" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonen" onclick="window.location=this.dataset.href" rel="nofollow">stonen</a>
          </span>
          <span class="term-help" data-term="stonen"><a href="/pebble#define=stonen" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3156" data-relevance="332" data-term="alcatraz" data-encoded-term="alcatraz" data-term-stats="1	0.6	0.000	3156	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/alcatraz" onclick="window.location=this.dataset.href" rel="nofollow">alcatraz</a>
          </span>
          <span class="term-help" data-term="alcatraz"><a href="/pebble#define=alcatraz" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="828" data-relevance="331" data-term="spongy" data-encoded-term="spongy" data-term-stats="1	0.6	0.000	828	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spongy" onclick="window.location=this.dataset.href" rel="nofollow">spongy</a>
          </span>
          <span class="term-help" data-term="spongy"><a href="/pebble#define=spongy" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="257" data-relevance="330" data-term="rockery" data-encoded-term="rockery" data-term-stats="1	0.6	0.000	257	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockery" onclick="window.location=this.dataset.href" rel="nofollow">rockery</a>
          </span>
          <span class="term-help" data-term="rockery"><a href="/pebble#define=rockery" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4301" data-relevance="329" data-term="touchstone" data-encoded-term="touchstone" data-term-stats="1	0.6	0.000	4301	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/touchstone" onclick="window.location=this.dataset.href" rel="nofollow">touchstone</a>
          </span>
          <span class="term-help" data-term="touchstone"><a href="/pebble#define=touchstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="328" data-term="rupestral" data-encoded-term="rupestral" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rupestral" onclick="window.location=this.dataset.href" rel="nofollow">rupestral</a>
          </span>
          <span class="term-help" data-term="rupestral"><a href="/pebble#define=rupestral" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="18305" data-relevance="327" data-term="tor" data-encoded-term="tor" data-term-stats="1	0.6	0.000	18305	cn5|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tor" onclick="window.location=this.dataset.href" rel="nofollow">tor</a>
          </span>
          <span class="term-help" data-term="tor"><a href="/pebble#define=tor" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="10604" data-relevance="326" data-term="cornerstone" data-encoded-term="cornerstone" data-term-stats="1	0.6	0.000	10604	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cornerstone" onclick="window.location=this.dataset.href" rel="nofollow">cornerstone</a>
          </span>
          <span class="term-help" data-term="cornerstone"><a href="/pebble#define=cornerstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="37" data-relevance="325" data-term="lithiasis" data-encoded-term="lithiasis" data-term-stats="1	0.6	0.000	37	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lithiasis" onclick="window.location=this.dataset.href" rel="nofollow">lithiasis</a>
          </span>
          <span class="term-help" data-term="lithiasis"><a href="/pebble#define=lithiasis" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="215" data-relevance="324" data-term="greisen" data-encoded-term="greisen" data-term-stats="1	0.6	0.000	215	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/greisen" onclick="window.location=this.dataset.href" rel="nofollow">greisen</a>
          </span>
          <span class="term-help" data-term="greisen"><a href="/pebble#define=greisen" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4246" data-relevance="323" data-term="magma" data-encoded-term="magma" data-term-stats="1	0.6	0.000	4246	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/magma" onclick="window.location=this.dataset.href" rel="nofollow">magma</a>
          </span>
          <span class="term-help" data-term="magma"><a href="/pebble#define=magma" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="322" data-term="stonecast" data-encoded-term="stonecast" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonecast" onclick="window.location=this.dataset.href" rel="nofollow">stonecast</a>
          </span>
          <span class="term-help" data-term="stonecast"><a href="/pebble#define=stonecast" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="321" data-term="alternarock" data-encoded-term="alternarock" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/alternarock" onclick="window.location=this.dataset.href" rel="nofollow">alternarock</a>
          </span>
          <span class="term-help" data-term="alternarock"><a href="/pebble#define=alternarock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="208" data-relevance="320" data-term="ragstone" data-encoded-term="ragstone" data-term-stats="1	0.6	0.000	208	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ragstone" onclick="window.location=this.dataset.href" rel="nofollow">ragstone</a>
          </span>
          <span class="term-help" data-term="ragstone"><a href="/pebble#define=ragstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="371" data-relevance="319" data-term="chondrite" data-encoded-term="chondrite" data-term-stats="1	0.6	0.000	371	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/chondrite" onclick="window.location=this.dataset.href" rel="nofollow">chondrite</a>
          </span>
          <span class="term-help" data-term="chondrite"><a href="/pebble#define=chondrite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="60" data-relevance="318" data-term="epilithic" data-encoded-term="epilithic" data-term-stats="1	0.6	0.000	60	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/epilithic" onclick="window.location=this.dataset.href" rel="nofollow">epilithic</a>
          </span>
          <span class="term-help" data-term="epilithic"><a href="/pebble#define=epilithic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="37" data-relevance="317" data-term="rockish" data-encoded-term="rockish" data-term-stats="1	0.6	0.000	37	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockish" onclick="window.location=this.dataset.href" rel="nofollow">rockish</a>
          </span>
          <span class="term-help" data-term="rockish"><a href="/pebble#define=rockish" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="316" data-term="rockscape" data-encoded-term="rockscape" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockscape" onclick="window.location=this.dataset.href" rel="nofollow">rockscape</a>
          </span>
          <span class="term-help" data-term="rockscape"><a href="/pebble#define=rockscape" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4644" data-relevance="315" data-term="gravestone" data-encoded-term="gravestone" data-term-stats="1	0.6	0.000	4644	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gravestone" onclick="window.location=this.dataset.href" rel="nofollow">gravestone</a>
          </span>
          <span class="term-help" data-term="gravestone"><a href="/pebble#define=gravestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="19096" data-relevance="314" data-term="milestone" data-encoded-term="milestone" data-term-stats="1	0.6	0.000	19096	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/milestone" onclick="window.location=this.dataset.href" rel="nofollow">milestone</a>
          </span>
          <span class="term-help" data-term="milestone"><a href="/pebble#define=milestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="40" data-relevance="313" data-term="britrock" data-encoded-term="britrock" data-term-stats="1	0.6	0.000	40	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/britrock" onclick="window.location=this.dataset.href" rel="nofollow">britrock</a>
          </span>
          <span class="term-help" data-term="britrock"><a href="/pebble#define=britrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="312" data-term="bondstone" data-encoded-term="bondstone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bondstone" onclick="window.location=this.dataset.href" rel="nofollow">bondstone</a>
          </span>
          <span class="term-help" data-term="bondstone"><a href="/pebble#define=bondstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3702" data-relevance="311" data-term="rockabilly" data-encoded-term="rockabilly" data-term-stats="1	0.6	0.000	3702	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockabilly" onclick="window.location=this.dataset.href" rel="nofollow">rockabilly</a>
          </span>
          <span class="term-help" data-term="rockabilly"><a href="/pebble#define=rockabilly" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="310" data-term="stonelike" data-encoded-term="stonelike" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonelike" onclick="window.location=this.dataset.href" rel="nofollow">stonelike</a>
          </span>
          <span class="term-help" data-term="stonelike"><a href="/pebble#define=stonelike" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1846" data-relevance="309" data-term="quartzite" data-encoded-term="quartzite" data-term-stats="1	0.6	0.000	1846	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/quartzite" onclick="window.location=this.dataset.href" rel="nofollow">quartzite</a>
          </span>
          <span class="term-help" data-term="quartzite"><a href="/pebble#define=quartzite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="84" data-relevance="308" data-term="achondrite" data-encoded-term="achondrite" data-term-stats="1	0.6	0.000	84	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/achondrite" onclick="window.location=this.dataset.href" rel="nofollow">achondrite</a>
          </span>
          <span class="term-help" data-term="achondrite"><a href="/pebble#define=achondrite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="56" data-relevance="307" data-term="xenolith" data-encoded-term="xenolith" data-term-stats="1	0.6	0.000	56	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/xenolith" onclick="window.location=this.dataset.href" rel="nofollow">xenolith</a>
          </span>
          <span class="term-help" data-term="xenolith"><a href="/pebble#define=xenolith" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1574" data-relevance="306" data-term="bluestone" data-encoded-term="bluestone" data-term-stats="1	0.6	0.000	1574	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bluestone" onclick="window.location=this.dataset.href" rel="nofollow">bluestone</a>
          </span>
          <span class="term-help" data-term="bluestone"><a href="/pebble#define=bluestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="305" data-term="rockily" data-encoded-term="rockily" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockily" onclick="window.location=this.dataset.href" rel="nofollow">rockily</a>
          </span>
          <span class="term-help" data-term="rockily"><a href="/pebble#define=rockily" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="169" data-relevance="304" data-term="rockness" data-encoded-term="rockness" data-term-stats="1	0.6	0.000	169	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockness" onclick="window.location=this.dataset.href" rel="nofollow">rockness</a>
          </span>
          <span class="term-help" data-term="rockness"><a href="/pebble#define=rockness" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2903" data-relevance="303" data-term="stonehenge" data-encoded-term="stonehenge" data-term-stats="1	0.6	0.000	2903	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonehenge" onclick="window.location=this.dataset.href" rel="nofollow">stonehenge</a>
          </span>
          <span class="term-help" data-term="stonehenge"><a href="/pebble#define=stonehenge" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="302" data-term="technorock" data-encoded-term="technorock" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/technorock" onclick="window.location=this.dataset.href" rel="nofollow">technorock</a>
          </span>
          <span class="term-help" data-term="technorock"><a href="/pebble#define=technorock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="301" data-term="gneissoid" data-encoded-term="gneissoid" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gneissoid" onclick="window.location=this.dataset.href" rel="nofollow">gneissoid</a>
          </span>
          <span class="term-help" data-term="gneissoid"><a href="/pebble#define=gneissoid" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="300" data-term="rocklike" data-encoded-term="rocklike" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rocklike" onclick="window.location=this.dataset.href" rel="nofollow">rocklike</a>
          </span>
          <span class="term-help" data-term="rocklike"><a href="/pebble#define=rocklike" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="299" data-term="granolith" data-encoded-term="granolith" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/granolith" onclick="window.location=this.dataset.href" rel="nofollow">granolith</a>
          </span>
          <span class="term-help" data-term="granolith"><a href="/pebble#define=granolith" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="76" data-relevance="298" data-term="stonebreaker" data-encoded-term="stonebreaker" data-term-stats="1	0.6	0.000	76	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonebreaker" onclick="window.location=this.dataset.href" rel="nofollow">stonebreaker</a>
          </span>
          <span class="term-help" data-term="stonebreaker"><a href="/pebble#define=stonebreaker" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="297" data-term="lithoid" data-encoded-term="lithoid" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lithoid" onclick="window.location=this.dataset.href" rel="nofollow">lithoid</a>
          </span>
          <span class="term-help" data-term="lithoid"><a href="/pebble#define=lithoid" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3359" data-relevance="296" data-term="outcrop" data-encoded-term="outcrop" data-term-stats="1	0.6	0.000	3359	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/outcrop" onclick="window.location=this.dataset.href" rel="nofollow">outcrop</a>
          </span>
          <span class="term-help" data-term="outcrop"><a href="/pebble#define=outcrop" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="88" data-relevance="295" data-term="dolostone" data-encoded-term="dolostone" data-term-stats="1	0.6	0.000	88	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dolostone" onclick="window.location=this.dataset.href" rel="nofollow">dolostone</a>
          </span>
          <span class="term-help" data-term="dolostone"><a href="/pebble#define=dolostone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="58" data-relevance="294" data-term="stonebow" data-encoded-term="stonebow" data-term-stats="1	0.6	0.000	58	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonebow" onclick="window.location=this.dataset.href" rel="nofollow">stonebow</a>
          </span>
          <span class="term-help" data-term="stonebow"><a href="/pebble#define=stonebow" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="293" data-term="lapidate" data-encoded-term="lapidate" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lapidate" onclick="window.location=this.dataset.href" rel="nofollow">lapidate</a>
          </span>
          <span class="term-help" data-term="lapidate"><a href="/pebble#define=lapidate" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5124" data-relevance="292" data-term="intrusion" data-encoded-term="intrusion" data-term-stats="1	0.6	0.000	5124	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/intrusion" onclick="window.location=this.dataset.href" rel="nofollow">intrusion</a>
          </span>
          <span class="term-help" data-term="intrusion"><a href="/pebble#define=intrusion" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="840" data-relevance="291" data-term="sedimentology" data-encoded-term="sedimentology" data-term-stats="1	0.6	0.000	840	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sedimentology" onclick="window.location=this.dataset.href" rel="nofollow">sedimentology</a>
          </span>
          <span class="term-help" data-term="sedimentology"><a href="/pebble#define=sedimentology" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="22438" data-relevance="290" data-term="flint" data-encoded-term="flint" data-term-stats="1	0.6	0.000	22438	swiki|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flint" onclick="window.location=this.dataset.href" rel="nofollow">flint</a>
          </span>
          <span class="term-help" data-term="flint"><a href="/pebble#define=flint" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="435" data-relevance="289" data-term="rockpile" data-encoded-term="rockpile" data-term-stats="1	0.6	0.000	435	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockpile" onclick="window.location=this.dataset.href" rel="nofollow">rockpile</a>
          </span>
          <span class="term-help" data-term="rockpile"><a href="/pebble#define=rockpile" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2181" data-relevance="288" data-term="aquifer" data-encoded-term="aquifer" data-term-stats="1	0.6	0.000	2181	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/aquifer" onclick="window.location=this.dataset.href" rel="nofollow">aquifer</a>
          </span>
          <span class="term-help" data-term="aquifer"><a href="/pebble#define=aquifer" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="119" data-relevance="287" data-term="lapstone" data-encoded-term="lapstone" data-term-stats="1	0.6	0.000	119	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lapstone" onclick="window.location=this.dataset.href" rel="nofollow">lapstone</a>
          </span>
          <span class="term-help" data-term="lapstone"><a href="/pebble#define=lapstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="44594" data-relevance="286" data-term="aa" data-encoded-term="aa" data-term-stats="1	0.6	0.000	44594	cn5|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/aa" onclick="window.location=this.dataset.href" rel="nofollow">aa</a>
          </span>
          <span class="term-help" data-term="aa"><a href="/pebble#define=aa" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4519" data-relevance="285" data-term="garnet" data-encoded-term="garnet" data-term-stats="1	0.6	0.000	4519	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/garnet" onclick="window.location=this.dataset.href" rel="nofollow">garnet</a>
          </span>
          <span class="term-help" data-term="garnet"><a href="/pebble#define=garnet" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1819" data-relevance="284" data-term="capstone" data-encoded-term="capstone" data-term-stats="1	0.6	0.000	1819	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/capstone" onclick="window.location=this.dataset.href" rel="nofollow">capstone</a>
          </span>
          <span class="term-help" data-term="capstone"><a href="/pebble#define=capstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="283" data-term="nutate" data-encoded-term="nutate" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nutate" onclick="window.location=this.dataset.href" rel="nofollow">nutate</a>
          </span>
          <span class="term-help" data-term="nutate"><a href="/pebble#define=nutate" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="135" data-relevance="282" data-term="arkose" data-encoded-term="arkose" data-term-stats="1	0.6	0.000	135	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/arkose" onclick="window.location=this.dataset.href" rel="nofollow">arkose</a>
          </span>
          <span class="term-help" data-term="arkose"><a href="/pebble#define=arkose" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="130" data-relevance="281" data-term="phosphorite" data-encoded-term="phosphorite" data-term-stats="1	0.6	0.000	130	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/phosphorite" onclick="window.location=this.dataset.href" rel="nofollow">phosphorite</a>
          </span>
          <span class="term-help" data-term="phosphorite"><a href="/pebble#define=phosphorite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="280" data-term="ventifact" data-encoded-term="ventifact" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ventifact" onclick="window.location=this.dataset.href" rel="nofollow">ventifact</a>
          </span>
          <span class="term-help" data-term="ventifact"><a href="/pebble#define=ventifact" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="279" data-term="adularia" data-encoded-term="adularia" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/adularia" onclick="window.location=this.dataset.href" rel="nofollow">adularia</a>
          </span>
          <span class="term-help" data-term="adularia"><a href="/pebble#define=adularia" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="278" data-term="stonelayer" data-encoded-term="stonelayer" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonelayer" onclick="window.location=this.dataset.href" rel="nofollow">stonelayer</a>
          </span>
          <span class="term-help" data-term="stonelayer"><a href="/pebble#define=stonelayer" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="60" data-relevance="277" data-term="trilithon" data-encoded-term="trilithon" data-term-stats="1	0.6	0.000	60	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/trilithon" onclick="window.location=this.dataset.href" rel="nofollow">trilithon</a>
          </span>
          <span class="term-help" data-term="trilithon"><a href="/pebble#define=trilithon" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="276" data-term="chuckstone" data-encoded-term="chuckstone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/chuckstone" onclick="window.location=this.dataset.href" rel="nofollow">chuckstone</a>
          </span>
          <span class="term-help" data-term="chuckstone"><a href="/pebble#define=chuckstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="562" data-relevance="275" data-term="datestone" data-encoded-term="datestone" data-term-stats="1	0.6	0.000	562	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/datestone" onclick="window.location=this.dataset.href" rel="nofollow">datestone</a>
          </span>
          <span class="term-help" data-term="datestone"><a href="/pebble#define=datestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="274" data-term="oilstone" data-encoded-term="oilstone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oilstone" onclick="window.location=this.dataset.href" rel="nofollow">oilstone</a>
          </span>
          <span class="term-help" data-term="oilstone"><a href="/pebble#define=oilstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="273" data-term="tilestone" data-encoded-term="tilestone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tilestone" onclick="window.location=this.dataset.href" rel="nofollow">tilestone</a>
          </span>
          <span class="term-help" data-term="tilestone"><a href="/pebble#define=tilestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="272" data-term="dropstone" data-encoded-term="dropstone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dropstone" onclick="window.location=this.dataset.href" rel="nofollow">dropstone</a>
          </span>
          <span class="term-help" data-term="dropstone"><a href="/pebble#define=dropstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="271" data-term="aphanite" data-encoded-term="aphanite" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/aphanite" onclick="window.location=this.dataset.href" rel="nofollow">aphanite</a>
          </span>
          <span class="term-help" data-term="aphanite"><a href="/pebble#define=aphanite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="221" data-relevance="270" data-term="hardstone" data-encoded-term="hardstone" data-term-stats="1	0.6	0.000	221	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hardstone" onclick="window.location=this.dataset.href" rel="nofollow">hardstone</a>
          </span>
          <span class="term-help" data-term="hardstone"><a href="/pebble#define=hardstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="58" data-relevance="269" data-term="wackestone" data-encoded-term="wackestone" data-term-stats="1	0.6	0.000	58	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/wackestone" onclick="window.location=this.dataset.href" rel="nofollow">wackestone</a>
          </span>
          <span class="term-help" data-term="wackestone"><a href="/pebble#define=wackestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1760" data-relevance="268" data-term="riverbed" data-encoded-term="riverbed" data-term-stats="1	0.6	0.000	1760	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/riverbed" onclick="window.location=this.dataset.href" rel="nofollow">riverbed</a>
          </span>
          <span class="term-help" data-term="riverbed"><a href="/pebble#define=riverbed" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="267" data-term="bytownite" data-encoded-term="bytownite" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bytownite" onclick="window.location=this.dataset.href" rel="nofollow">bytownite</a>
          </span>
          <span class="term-help" data-term="bytownite"><a href="/pebble#define=bytownite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="266" data-term="rockiness" data-encoded-term="rockiness" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockiness" onclick="window.location=this.dataset.href" rel="nofollow">rockiness</a>
          </span>
          <span class="term-help" data-term="rockiness"><a href="/pebble#define=rockiness" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="265" data-term="bafflestone" data-encoded-term="bafflestone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bafflestone" onclick="window.location=this.dataset.href" rel="nofollow">bafflestone</a>
          </span>
          <span class="term-help" data-term="bafflestone"><a href="/pebble#define=bafflestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="259" data-relevance="264" data-term="rockfill" data-encoded-term="rockfill" data-term-stats="1	0.6	0.000	259	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockfill" onclick="window.location=this.dataset.href" rel="nofollow">rockfill</a>
          </span>
          <span class="term-help" data-term="rockfill"><a href="/pebble#define=rockfill" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="263" data-term="crowstone" data-encoded-term="crowstone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/crowstone" onclick="window.location=this.dataset.href" rel="nofollow">crowstone</a>
          </span>
          <span class="term-help" data-term="crowstone"><a href="/pebble#define=crowstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="602" data-relevance="262" data-term="rhinestone" data-encoded-term="rhinestone" data-term-stats="1	0.6	0.000	602	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rhinestone" onclick="window.location=this.dataset.href" rel="nofollow">rhinestone</a>
          </span>
          <span class="term-help" data-term="rhinestone"><a href="/pebble#define=rhinestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="261" data-term="floatstone" data-encoded-term="floatstone" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/floatstone" onclick="window.location=this.dataset.href" rel="nofollow">floatstone</a>
          </span>
          <span class="term-help" data-term="floatstone"><a href="/pebble#define=floatstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="117" data-relevance="260" data-term="roadstone" data-encoded-term="roadstone" data-term-stats="1	0.6	0.000	117	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/roadstone" onclick="window.location=this.dataset.href" rel="nofollow">roadstone</a>
          </span>
          <span class="term-help" data-term="roadstone"><a href="/pebble#define=roadstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="79" data-relevance="259" data-term="anorthite" data-encoded-term="anorthite" data-term-stats="1	0.6	0.000	79	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/anorthite" onclick="window.location=this.dataset.href" rel="nofollow">anorthite</a>
          </span>
          <span class="term-help" data-term="anorthite"><a href="/pebble#define=anorthite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="269" data-relevance="258" data-term="striation" data-encoded-term="striation" data-term-stats="1	0.6	0.000	269	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/striation" onclick="window.location=this.dataset.href" rel="nofollow">striation</a>
          </span>
          <span class="term-help" data-term="striation"><a href="/pebble#define=striation" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="257" data-term="poikilitic" data-encoded-term="poikilitic" data-term-stats="1	0.6	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/poikilitic" onclick="window.location=this.dataset.href" rel="nofollow">poikilitic</a>
          </span>
          <span class="term-help" data-term="poikilitic"><a href="/pebble#define=poikilitic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="457" data-relevance="256" data-term="sial" data-encoded-term="sial" data-term-stats="1	0.6	0.000	457	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sial" onclick="window.location=this.dataset.href" rel="nofollow">sial</a>
          </span>
          <span class="term-help" data-term="sial"><a href="/pebble#define=sial" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="315" data-relevance="255" data-term="pegmatite" data-encoded-term="pegmatite" data-term-stats="1	0.6	0.000	315	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pegmatite" onclick="window.location=this.dataset.href" rel="nofollow">pegmatite</a>
          </span>
          <span class="term-help" data-term="pegmatite"><a href="/pebble#define=pegmatite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="100" data-relevance="254" data-term="calcrete" data-encoded-term="calcrete" data-term-stats="1	0.6	0.000	100	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/calcrete" onclick="window.location=this.dataset.href" rel="nofollow">calcrete</a>
          </span>
          <span class="term-help" data-term="calcrete"><a href="/pebble#define=calcrete" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="60" data-relevance="253" data-term="packstone" data-encoded-term="packstone" data-term-stats="1	0.5	0.000	60	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/packstone" onclick="window.location=this.dataset.href" rel="nofollow">packstone</a>
          </span>
          <span class="term-help" data-term="packstone"><a href="/pebble#define=packstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="73" data-relevance="252" data-term="rockwork" data-encoded-term="rockwork" data-term-stats="1	0.5	0.000	73	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rockwork" onclick="window.location=this.dataset.href" rel="nofollow">rockwork</a>
          </span>
          <span class="term-help" data-term="rockwork"><a href="/pebble#define=rockwork" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="251" data-term="poikilotopic" data-encoded-term="poikilotopic" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/poikilotopic" onclick="window.location=this.dataset.href" rel="nofollow">poikilotopic</a>
          </span>
          <span class="term-help" data-term="poikilotopic"><a href="/pebble#define=poikilotopic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="77" data-relevance="250" data-term="birthstone" data-encoded-term="birthstone" data-term-stats="1	0.5	0.000	77	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/birthstone" onclick="window.location=this.dataset.href" rel="nofollow">birthstone</a>
          </span>
          <span class="term-help" data-term="birthstone"><a href="/pebble#define=birthstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="193" data-relevance="249" data-term="caliche" data-encoded-term="caliche" data-term-stats="1	0.5	0.000	193	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/caliche" onclick="window.location=this.dataset.href" rel="nofollow">caliche</a>
          </span>
          <span class="term-help" data-term="caliche"><a href="/pebble#define=caliche" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="248" data-term="topstone" data-encoded-term="topstone" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/topstone" onclick="window.location=this.dataset.href" rel="nofollow">topstone</a>
          </span>
          <span class="term-help" data-term="topstone"><a href="/pebble#define=topstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="247" data-term="dadrock" data-encoded-term="dadrock" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dadrock" onclick="window.location=this.dataset.href" rel="nofollow">dadrock</a>
          </span>
          <span class="term-help" data-term="dadrock"><a href="/pebble#define=dadrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="119" data-relevance="246" data-term="hornfels" data-encoded-term="hornfels" data-term-stats="1	0.5	0.000	119	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hornfels" onclick="window.location=this.dataset.href" rel="nofollow">hornfels</a>
          </span>
          <span class="term-help" data-term="hornfels"><a href="/pebble#define=hornfels" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="19781" data-relevance="245" data-term="armor" data-encoded-term="armor" data-term-stats="1	0.5	0.000	19781	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/armor" onclick="window.location=this.dataset.href" rel="nofollow">armor</a>
          </span>
          <span class="term-help" data-term="armor"><a href="/pebble#define=armor" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="244" data-term="irestone" data-encoded-term="irestone" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/irestone" onclick="window.location=this.dataset.href" rel="nofollow">irestone</a>
          </span>
          <span class="term-help" data-term="irestone"><a href="/pebble#define=irestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="992" data-relevance="243" data-term="doral" data-encoded-term="doral" data-term-stats="1	0.5	0.000	992	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/doral" onclick="window.location=this.dataset.href" rel="nofollow">doral</a>
          </span>
          <span class="term-help" data-term="doral"><a href="/pebble#define=doral" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="242" data-term="doorstone" data-encoded-term="doorstone" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/doorstone" onclick="window.location=this.dataset.href" rel="nofollow">doorstone</a>
          </span>
          <span class="term-help" data-term="doorstone"><a href="/pebble#define=doorstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="241" data-term="arenicolite" data-encoded-term="arenicolite" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/arenicolite" onclick="window.location=this.dataset.href" rel="nofollow">arenicolite</a>
          </span>
          <span class="term-help" data-term="arenicolite"><a href="/pebble#define=arenicolite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="130" data-relevance="240" data-term="stonefall" data-encoded-term="stonefall" data-term-stats="1	0.5	0.000	130	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonefall" onclick="window.location=this.dataset.href" rel="nofollow">stonefall</a>
          </span>
          <span class="term-help" data-term="stonefall"><a href="/pebble#define=stonefall" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="185" data-relevance="239" data-term="graystone" data-encoded-term="graystone" data-term-stats="1	0.5	0.000	185	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/graystone" onclick="window.location=this.dataset.href" rel="nofollow">graystone</a>
          </span>
          <span class="term-help" data-term="graystone"><a href="/pebble#define=graystone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="69039" data-relevance="238" data-term="golf" data-encoded-term="golf" data-term-stats="1	0.5	0.000	69039	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/golf" onclick="window.location=this.dataset.href" rel="nofollow">golf</a>
          </span>
          <span class="term-help" data-term="golf"><a href="/pebble#define=golf" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="172" data-relevance="237" data-term="petrous" data-encoded-term="petrous" data-term-stats="1	0.5	0.000	172	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/petrous" onclick="window.location=this.dataset.href" rel="nofollow">petrous</a>
          </span>
          <span class="term-help" data-term="petrous"><a href="/pebble#define=petrous" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="236" data-term="acrolith" data-encoded-term="acrolith" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/acrolith" onclick="window.location=this.dataset.href" rel="nofollow">acrolith</a>
          </span>
          <span class="term-help" data-term="acrolith"><a href="/pebble#define=acrolith" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="235" data-term="stonehard" data-encoded-term="stonehard" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonehard" onclick="window.location=this.dataset.href" rel="nofollow">stonehard</a>
          </span>
          <span class="term-help" data-term="stonehard"><a href="/pebble#define=stonehard" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="58" data-relevance="234" data-term="oligoclase" data-encoded-term="oligoclase" data-term-stats="1	0.5	0.000	58	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oligoclase" onclick="window.location=this.dataset.href" rel="nofollow">oligoclase</a>
          </span>
          <span class="term-help" data-term="oligoclase"><a href="/pebble#define=oligoclase" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="17552" data-relevance="233" data-term="invitational" data-encoded-term="invitational" data-term-stats="1	0.5	0.000	17552	w2v|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/invitational" onclick="window.location=this.dataset.href" rel="nofollow">invitational</a>
          </span>
          <span class="term-help" data-term="invitational"><a href="/pebble#define=invitational" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="76" data-relevance="232" data-term="clastic rocks" data-encoded-term="clastic%20rocks" data-term-stats="1	0.5	0.000	76	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/clastic-rocks" onclick="window.location=this.dataset.href" rel="nofollow">clastic rocks</a>
          </span>
          <span class="term-help" data-term="clastic rocks"><a href="/pebble#define=clastic rocks" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="357" data-relevance="231" data-term="oldowan" data-encoded-term="oldowan" data-term-stats="1	0.5	0.000	357	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oldowan" onclick="window.location=this.dataset.href" rel="nofollow">oldowan</a>
          </span>
          <span class="term-help" data-term="oldowan"><a href="/pebble#define=oldowan" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="230" data-term="diaclasis" data-encoded-term="diaclasis" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/diaclasis" onclick="window.location=this.dataset.href" rel="nofollow">diaclasis</a>
          </span>
          <span class="term-help" data-term="diaclasis"><a href="/pebble#define=diaclasis" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="299" data-relevance="229" data-term="hammerstone" data-encoded-term="hammerstone" data-term-stats="1	0.5	0.000	299	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hammerstone" onclick="window.location=this.dataset.href" rel="nofollow">hammerstone</a>
          </span>
          <span class="term-help" data-term="hammerstone"><a href="/pebble#define=hammerstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="515" data-relevance="228" data-term="clastic" data-encoded-term="clastic" data-term-stats="1	0.5	0.000	515	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/clastic" onclick="window.location=this.dataset.href" rel="nofollow">clastic</a>
          </span>
          <span class="term-help" data-term="clastic"><a href="/pebble#define=clastic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1610" data-relevance="227" data-term="compacted" data-encoded-term="compacted" data-term-stats="1	0.5	0.000	1610	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/compacted" onclick="window.location=this.dataset.href" rel="nofollow">compacted</a>
          </span>
          <span class="term-help" data-term="compacted"><a href="/pebble#define=compacted" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1417" data-relevance="226" data-term="tpc" data-encoded-term="tpc" data-term-stats="1	0.5	0.000	1417	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tpc" onclick="window.location=this.dataset.href" rel="nofollow">tpc</a>
          </span>
          <span class="term-help" data-term="tpc"><a href="/pebble#define=tpc" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="143" data-relevance="225" data-term="gallstone" data-encoded-term="gallstone" data-term-stats="1	0.5	0.000	143	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gallstone" onclick="window.location=this.dataset.href" rel="nofollow">gallstone</a>
          </span>
          <span class="term-help" data-term="gallstone"><a href="/pebble#define=gallstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="78566" data-relevance="224" data-term="woods" data-encoded-term="woods" data-term-stats="1	0.5	0.000	78566	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/woods" onclick="window.location=this.dataset.href" rel="nofollow">woods</a>
          </span>
          <span class="term-help" data-term="woods"><a href="/pebble#define=woods" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3069" data-relevance="223" data-term="sugarloaf" data-encoded-term="sugarloaf" data-term-stats="1	0.5	0.000	3069	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sugarloaf" onclick="window.location=this.dataset.href" rel="nofollow">sugarloaf</a>
          </span>
          <span class="term-help" data-term="sugarloaf"><a href="/pebble#define=sugarloaf" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="222" data-term="stonecraft" data-encoded-term="stonecraft" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonecraft" onclick="window.location=this.dataset.href" rel="nofollow">stonecraft</a>
          </span>
          <span class="term-help" data-term="stonecraft"><a href="/pebble#define=stonecraft" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="179" data-relevance="221" data-term="aterian" data-encoded-term="aterian" data-term-stats="1	0.5	0.000	179	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/aterian" onclick="window.location=this.dataset.href" rel="nofollow">aterian</a>
          </span>
          <span class="term-help" data-term="aterian"><a href="/pebble#define=aterian" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="63" data-relevance="220" data-term="saxicolous" data-encoded-term="saxicolous" data-term-stats="1	0.5	0.000	63	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/saxicolous" onclick="window.location=this.dataset.href" rel="nofollow">saxicolous</a>
          </span>
          <span class="term-help" data-term="saxicolous"><a href="/pebble#define=saxicolous" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="219" data-term="merestone" data-encoded-term="merestone" data-term-stats="1	0.5	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/merestone" onclick="window.location=this.dataset.href" rel="nofollow">merestone</a>
          </span>
          <span class="term-help" data-term="merestone"><a href="/pebble#define=merestone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="230" data-relevance="218" data-term="deathrock" data-encoded-term="deathrock" data-term-stats="1	0.5	0.000	230	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/deathrock" onclick="window.location=this.dataset.href" rel="nofollow">deathrock</a>
          </span>
          <span class="term-help" data-term="deathrock"><a href="/pebble#define=deathrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="312" data-relevance="217" data-term="stonechat" data-encoded-term="stonechat" data-term-stats="1	0.5	0.000	312	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stonechat" onclick="window.location=this.dataset.href" rel="nofollow">stonechat</a>
          </span>
          <span class="term-help" data-term="stonechat"><a href="/pebble#define=stonechat" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="442" data-relevance="216" data-term="small rock" data-encoded-term="small%20rock" data-term-stats="1	0.5	0.000	442	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/small-rock" onclick="window.location=this.dataset.href" rel="nofollow">small rock</a>
          </span>
          <span class="term-help" data-term="small rock"><a href="/pebble#define=small rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2755" data-relevance="215" data-term="lpga" data-encoded-term="lpga" data-term-stats="1	0.5	0.000	2755	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lpga" onclick="window.location=this.dataset.href" rel="nofollow">lpga</a>
          </span>
          <span class="term-help" data-term="lpga"><a href="/pebble#define=lpga" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="129133" data-relevance="214" data-term="ball" data-encoded-term="ball" data-term-stats="1	0.5	0.000	129133	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ball" onclick="window.location=this.dataset.href" rel="nofollow">ball</a>
          </span>
          <span class="term-help" data-term="ball"><a href="/pebble#define=ball" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="491" data-relevance="213" data-term="hazeltine" data-encoded-term="hazeltine" data-term-stats="1	0.5	0.000	491	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hazeltine" onclick="window.location=this.dataset.href" rel="nofollow">hazeltine</a>
          </span>
          <span class="term-help" data-term="hazeltine"><a href="/pebble#define=hazeltine" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9711" data-relevance="212" data-term="pga" data-encoded-term="pga" data-term-stats="1	0.5	0.000	9711	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pga" onclick="window.location=this.dataset.href" rel="nofollow">pga</a>
          </span>
          <span class="term-help" data-term="pga"><a href="/pebble#define=pga" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="25300" data-relevance="211" data-term="oaks" data-encoded-term="oaks" data-term-stats="1	0.5	0.000	25300	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oaks" onclick="window.location=this.dataset.href" rel="nofollow">oaks</a>
          </span>
          <span class="term-help" data-term="oaks"><a href="/pebble#define=oaks" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1702" data-relevance="210" data-term="mickelson" data-encoded-term="mickelson" data-term-stats="1	0.5	0.000	1702	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/mickelson" onclick="window.location=this.dataset.href" rel="nofollow">mickelson</a>
          </span>
          <span class="term-help" data-term="mickelson"><a href="/pebble#define=mickelson" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="7872" data-relevance="209" data-term="scottsdale" data-encoded-term="scottsdale" data-term-stats="1	0.5	0.000	7872	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/scottsdale" onclick="window.location=this.dataset.href" rel="nofollow">scottsdale</a>
          </span>
          <span class="term-help" data-term="scottsdale"><a href="/pebble#define=scottsdale" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1099" data-relevance="208" data-term="bethpage" data-encoded-term="bethpage" data-term-stats="1	0.5	0.000	1099	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bethpage" onclick="window.location=this.dataset.href" rel="nofollow">bethpage</a>
          </span>
          <span class="term-help" data-term="bethpage"><a href="/pebble#define=bethpage" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="23705" data-relevance="207" data-term="belmont" data-encoded-term="belmont" data-term-stats="1	0.5	0.000	23705	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/belmont" onclick="window.location=this.dataset.href" rel="nofollow">belmont</a>
          </span>
          <span class="term-help" data-term="belmont"><a href="/pebble#define=belmont" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="438" data-relevance="206" data-term="carnoustie" data-encoded-term="carnoustie" data-term-stats="1	0.5	0.000	438	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/carnoustie" onclick="window.location=this.dataset.href" rel="nofollow">carnoustie</a>
          </span>
          <span class="term-help" data-term="carnoustie"><a href="/pebble#define=carnoustie" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2862" data-relevance="205" data-term="pocono" data-encoded-term="pocono" data-term-stats="1	0.5	0.000	2862	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pocono" onclick="window.location=this.dataset.href" rel="nofollow">pocono</a>
          </span>
          <span class="term-help" data-term="pocono"><a href="/pebble#define=pocono" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="576" data-relevance="204" data-term="grain size" data-encoded-term="grain%20size" data-term-stats="1	0.5	0.000	576	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/grain-size" onclick="window.location=this.dataset.href" rel="nofollow">grain size</a>
          </span>
          <span class="term-help" data-term="grain size"><a href="/pebble#define=grain size" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="27284" data-relevance="203" data-term="meadows" data-encoded-term="meadows" data-term-stats="1	0.5	0.000	27284	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/meadows" onclick="window.location=this.dataset.href" rel="nofollow">meadows</a>
          </span>
          <span class="term-help" data-term="meadows"><a href="/pebble#define=meadows" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2305" data-relevance="202" data-term="hammock" data-encoded-term="hammock" data-term-stats="1	0.4	0.000	2305	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hammock" onclick="window.location=this.dataset.href" rel="nofollow">hammock</a>
          </span>
          <span class="term-help" data-term="hammock"><a href="/pebble#define=hammock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4192" data-relevance="201" data-term="buick" data-encoded-term="buick" data-term-stats="1	0.4	0.000	4192	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/buick" onclick="window.location=this.dataset.href" rel="nofollow">buick</a>
          </span>
          <span class="term-help" data-term="buick"><a href="/pebble#define=buick" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="10267" data-relevance="200" data-term="rubble" data-encoded-term="rubble" data-term-stats="1	0.4	0.000	10267	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rubble" onclick="window.location=this.dataset.href" rel="nofollow">rubble</a>
          </span>
          <span class="term-help" data-term="rubble"><a href="/pebble#define=rubble" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4288" data-relevance="199" data-term="torrey" data-encoded-term="torrey" data-term-stats="1	0.4	0.000	4288	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/torrey" onclick="window.location=this.dataset.href" rel="nofollow">torrey</a>
          </span>
          <span class="term-help" data-term="torrey"><a href="/pebble#define=torrey" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="121" data-relevance="198" data-term="blarney stone" data-encoded-term="blarney%20stone" data-term-stats="1	0.4	0.000	121	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/blarney-stone" onclick="window.location=this.dataset.href" rel="nofollow">blarney stone</a>
          </span>
          <span class="term-help" data-term="blarney stone"><a href="/pebble#define=blarney stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="11787" data-relevance="197" data-term="cypress" data-encoded-term="cypress" data-term-stats="1	0.4	0.000	11787	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cypress" onclick="window.location=this.dataset.href" rel="nofollow">cypress</a>
          </span>
          <span class="term-help" data-term="cypress"><a href="/pebble#define=cypress" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="133" data-relevance="196" data-term="dimension stone" data-encoded-term="dimension%20stone" data-term-stats="1	0.4	0.000	133	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dimension-stone" onclick="window.location=this.dataset.href" rel="nofollow">dimension stone</a>
          </span>
          <span class="term-help" data-term="dimension stone"><a href="/pebble#define=dimension stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2561" data-relevance="195" data-term="concours" data-encoded-term="concours" data-term-stats="1	0.4	0.000	2561	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/concours" onclick="window.location=this.dataset.href" rel="nofollow">concours</a>
          </span>
          <span class="term-help" data-term="concours"><a href="/pebble#define=concours" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="723" data-relevance="194" data-term="dry stone" data-encoded-term="dry%20stone" data-term-stats="1	0.4	0.000	723	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dry-stone" onclick="window.location=this.dataset.href" rel="nofollow">dry stone</a>
          </span>
          <span class="term-help" data-term="dry stone"><a href="/pebble#define=dry stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="614" data-relevance="193" data-term="birkdale" data-encoded-term="birkdale" data-term-stats="1	0.4	0.000	614	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/birkdale" onclick="window.location=this.dataset.href" rel="nofollow">birkdale</a>
          </span>
          <span class="term-help" data-term="birkdale"><a href="/pebble#define=birkdale" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9985" data-relevance="192" data-term="nonsense" data-encoded-term="nonsense" data-term-stats="1	0.4	0.000	9985	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nonsense" onclick="window.location=this.dataset.href" rel="nofollow">nonsense</a>
          </span>
          <span class="term-help" data-term="nonsense"><a href="/pebble#define=nonsense" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2471" data-relevance="191" data-term="caliente" data-encoded-term="caliente" data-term-stats="1	0.4	0.000	2471	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/caliente" onclick="window.location=this.dataset.href" rel="nofollow">caliente</a>
          </span>
          <span class="term-help" data-term="caliente"><a href="/pebble#define=caliente" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4375" data-relevance="190" data-term="biscayne" data-encoded-term="biscayne" data-term-stats="1	0.4	0.000	4375	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/biscayne" onclick="window.location=this.dataset.href" rel="nofollow">biscayne</a>
          </span>
          <span class="term-help" data-term="biscayne"><a href="/pebble#define=biscayne" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="12533" data-relevance="189" data-term="pines" data-encoded-term="pines" data-term-stats="1	0.4	0.000	12533	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pines" onclick="window.location=this.dataset.href" rel="nofollow">pines</a>
          </span>
          <span class="term-help" data-term="pines"><a href="/pebble#define=pines" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="13645" data-relevance="188" data-term="dunes" data-encoded-term="dunes" data-term-stats="1	0.4	0.000	13645	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dunes" onclick="window.location=this.dataset.href" rel="nofollow">dunes</a>
          </span>
          <span class="term-help" data-term="dunes"><a href="/pebble#define=dunes" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3859" data-relevance="187" data-term="toms" data-encoded-term="toms" data-term-stats="1	0.4	0.000	3859	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/toms" onclick="window.location=this.dataset.href" rel="nofollow">toms</a>
          </span>
          <span class="term-help" data-term="toms"><a href="/pebble#define=toms" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="139" data-relevance="186" data-term="stone deaf" data-encoded-term="stone%20deaf" data-term-stats="1	0.4	0.000	139	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stone-deaf" onclick="window.location=this.dataset.href" rel="nofollow">stone deaf</a>
          </span>
          <span class="term-help" data-term="stone deaf"><a href="/pebble#define=stone deaf" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="144960" data-relevance="185" data-term="pierre" data-encoded-term="pierre" data-term-stats="1	0.4	0.000	144960	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pierre" onclick="window.location=this.dataset.href" rel="nofollow">pierre</a>
          </span>
          <span class="term-help" data-term="pierre"><a href="/pebble#define=pierre" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1747" data-relevance="184" data-term="nicklaus" data-encoded-term="nicklaus" data-term-stats="1	0.4	0.000	1747	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nicklaus" onclick="window.location=this.dataset.href" rel="nofollow">nicklaus</a>
          </span>
          <span class="term-help" data-term="nicklaus"><a href="/pebble#define=nicklaus" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1032" data-relevance="183" data-term="prefontaine" data-encoded-term="prefontaine" data-term-stats="1	0.4	0.000	1032	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/prefontaine" onclick="window.location=this.dataset.href" rel="nofollow">prefontaine</a>
          </span>
          <span class="term-help" data-term="prefontaine"><a href="/pebble#define=prefontaine" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2525" data-relevance="182" data-term="candlestick" data-encoded-term="candlestick" data-term-stats="1	0.4	0.000	2525	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/candlestick" onclick="window.location=this.dataset.href" rel="nofollow">candlestick</a>
          </span>
          <span class="term-help" data-term="candlestick"><a href="/pebble#define=candlestick" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="663" data-relevance="181" data-term="rosetta stone" data-encoded-term="rosetta%20stone" data-term-stats="1	0.4	0.000	663	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rosetta-stone" onclick="window.location=this.dataset.href" rel="nofollow">rosetta stone</a>
          </span>
          <span class="term-help" data-term="rosetta stone"><a href="/pebble#define=rosetta stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4969" data-relevance="180" data-term="ginn" data-encoded-term="ginn" data-term-stats="1	0.4	0.000	4969	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ginn" onclick="window.location=this.dataset.href" rel="nofollow">ginn</a>
          </span>
          <span class="term-help" data-term="ginn"><a href="/pebble#define=ginn" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4586" data-relevance="179" data-term="delray" data-encoded-term="delray" data-term-stats="1	0.4	0.000	4586	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/delray" onclick="window.location=this.dataset.href" rel="nofollow">delray</a>
          </span>
          <span class="term-help" data-term="delray"><a href="/pebble#define=delray" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="17420" data-relevance="178" data-term="vein" data-encoded-term="vein" data-term-stats="1	0.4	0.000	17420	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/vein" onclick="window.location=this.dataset.href" rel="nofollow">vein</a>
          </span>
          <span class="term-help" data-term="vein"><a href="/pebble#define=vein" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3216" data-relevance="177" data-term="donington" data-encoded-term="donington" data-term-stats="1	0.4	0.000	3216	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/donington" onclick="window.location=this.dataset.href" rel="nofollow">donington</a>
          </span>
          <span class="term-help" data-term="donington"><a href="/pebble#define=donington" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="47236" data-relevance="176" data-term="rocket" data-encoded-term="rocket" data-term-stats="1	0.4	0.000	47236	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rocket" onclick="window.location=this.dataset.href" rel="nofollow">rocket</a>
          </span>
          <span class="term-help" data-term="rocket"><a href="/pebble#define=rocket" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="253" data-relevance="175" data-term="kidney stone" data-encoded-term="kidney%20stone" data-term-stats="1	0.4	0.000	253	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/kidney-stone" onclick="window.location=this.dataset.href" rel="nofollow">kidney stone</a>
          </span>
          <span class="term-help" data-term="kidney stone"><a href="/pebble#define=kidney stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1057" data-relevance="174" data-term="accenture" data-encoded-term="accenture" data-term-stats="1	0.4	0.000	1057	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/accenture" onclick="window.location=this.dataset.href" rel="nofollow">accenture</a>
          </span>
          <span class="term-help" data-term="accenture"><a href="/pebble#define=accenture" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4450" data-relevance="173" data-term="els" data-encoded-term="els" data-term-stats="1	0.4	0.000	4450	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/els" onclick="window.location=this.dataset.href" rel="nofollow">els</a>
          </span>
          <span class="term-help" data-term="els"><a href="/pebble#define=els" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="6549" data-relevance="172" data-term="racetrack" data-encoded-term="racetrack" data-term-stats="1	0.4	0.000	6549	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/racetrack" onclick="window.location=this.dataset.href" rel="nofollow">racetrack</a>
          </span>
          <span class="term-help" data-term="racetrack"><a href="/pebble#define=racetrack" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="18310" data-relevance="171" data-term="turf" data-encoded-term="turf" data-term-stats="1	0.4	0.000	18310	w2v|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/turf" onclick="window.location=this.dataset.href" rel="nofollow">turf</a>
          </span>
          <span class="term-help" data-term="turf"><a href="/pebble#define=turf" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="708" data-relevance="170" data-term="avp" data-encoded-term="avp" data-term-stats="1	0.4	0.000	708	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/avp" onclick="window.location=this.dataset.href" rel="nofollow">avp</a>
          </span>
          <span class="term-help" data-term="avp"><a href="/pebble#define=avp" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="169" data-term="roll stone" data-encoded-term="roll%20stone" data-term-stats="1	0.4	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/roll-stone" onclick="window.location=this.dataset.href" rel="nofollow">roll stone</a>
          </span>
          <span class="term-help" data-term="roll stone"><a href="/pebble#define=roll stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9529" data-relevance="168" data-term="magnolia" data-encoded-term="magnolia" data-term-stats="1	0.4	0.000	9529	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/magnolia" onclick="window.location=this.dataset.href" rel="nofollow">magnolia</a>
          </span>
          <span class="term-help" data-term="magnolia"><a href="/pebble#define=magnolia" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5612" data-relevance="167" data-term="canyons" data-encoded-term="canyons" data-term-stats="1	0.4	0.000	5612	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/canyons" onclick="window.location=this.dataset.href" rel="nofollow">canyons</a>
          </span>
          <span class="term-help" data-term="canyons"><a href="/pebble#define=canyons" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1580" data-relevance="166" data-term="conover" data-encoded-term="conover" data-term-stats="1	0.4	0.000	1580	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/conover" onclick="window.location=this.dataset.href" rel="nofollow">conover</a>
          </span>
          <span class="term-help" data-term="conover"><a href="/pebble#define=conover" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1326" data-relevance="165" data-term="bulle" data-encoded-term="bulle" data-term-stats="1	0.4	0.000	1326	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bulle" onclick="window.location=this.dataset.href" rel="nofollow">bulle</a>
          </span>
          <span class="term-help" data-term="bulle"><a href="/pebble#define=bulle" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2106" data-relevance="164" data-term="troon" data-encoded-term="troon" data-term-stats="1	0.4	0.000	2106	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/troon" onclick="window.location=this.dataset.href" rel="nofollow">troon</a>
          </span>
          <span class="term-help" data-term="troon"><a href="/pebble#define=troon" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1290" data-relevance="163" data-term="aami" data-encoded-term="aami" data-term-stats="1	0.4	0.000	1290	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/aami" onclick="window.location=this.dataset.href" rel="nofollow">aami</a>
          </span>
          <span class="term-help" data-term="aami"><a href="/pebble#define=aami" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="22471" data-relevance="162" data-term="hard rock" data-encoded-term="hard%20rock" data-term-stats="1	0.4	0.000	22471	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hard-rock" onclick="window.location=this.dataset.href" rel="nofollow">hard rock</a>
          </span>
          <span class="term-help" data-term="hard rock"><a href="/pebble#define=hard rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="161" data-term="röck döts" data-encoded-term="r%C3%B6ck%20d%C3%B6ts" data-term-stats="1	0.4	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/röck-döts" onclick="window.location=this.dataset.href" rel="nofollow">röck döts</a>
          </span>
          <span class="term-help" data-term="röck döts"><a href="/pebble#define=röck döts" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="969" data-relevance="160" data-term="stricker" data-encoded-term="stricker" data-term-stats="1	0.4	0.000	969	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stricker" onclick="window.location=this.dataset.href" rel="nofollow">stricker</a>
          </span>
          <span class="term-help" data-term="stricker"><a href="/pebble#define=stricker" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2788" data-relevance="159" data-term="lomond" data-encoded-term="lomond" data-term-stats="1	0.4	0.000	2788	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lomond" onclick="window.location=this.dataset.href" rel="nofollow">lomond</a>
          </span>
          <span class="term-help" data-term="lomond"><a href="/pebble#define=lomond" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="158" data-term="cast first stone" data-encoded-term="cast%20first%20stone" data-term-stats="1	0.4	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cast-first-stone" onclick="window.location=this.dataset.href" rel="nofollow">cast first stone</a>
          </span>
          <span class="term-help" data-term="cast first stone"><a href="/pebble#define=cast first stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1685" data-relevance="157" data-term="leaderboard" data-encoded-term="leaderboard" data-term-stats="1	0.4	0.000	1685	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/leaderboard" onclick="window.location=this.dataset.href" rel="nofollow">leaderboard</a>
          </span>
          <span class="term-help" data-term="leaderboard"><a href="/pebble#define=leaderboard" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1470" data-relevance="156" data-term="maurier" data-encoded-term="maurier" data-term-stats="1	0.4	0.000	1470	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/maurier" onclick="window.location=this.dataset.href" rel="nofollow">maurier</a>
          </span>
          <span class="term-help" data-term="maurier"><a href="/pebble#define=maurier" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="168978" data-relevance="155" data-term="classic" data-encoded-term="classic" data-term-stats="1	0.4	0.000	168978	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/classic" onclick="window.location=this.dataset.href" rel="nofollow">classic</a>
          </span>
          <span class="term-help" data-term="classic"><a href="/pebble#define=classic" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1843" data-relevance="154" data-term="chafes" data-encoded-term="chafes" data-term-stats="1	0.4	0.000	1843	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/chafes" onclick="window.location=this.dataset.href" rel="nofollow">chafes</a>
          </span>
          <span class="term-help" data-term="chafes"><a href="/pebble#define=chafes" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="7817" data-relevance="153" data-term="raceway" data-encoded-term="raceway" data-term-stats="1	0.4	0.000	7817	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/raceway" onclick="window.location=this.dataset.href" rel="nofollow">raceway</a>
          </span>
          <span class="term-help" data-term="raceway"><a href="/pebble#define=raceway" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4357" data-relevance="152" data-term="bighorn" data-encoded-term="bighorn" data-term-stats="1	0.4	0.000	4357	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bighorn" onclick="window.location=this.dataset.href" rel="nofollow">bighorn</a>
          </span>
          <span class="term-help" data-term="bighorn"><a href="/pebble#define=bighorn" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2251" data-relevance="151" data-term="deere" data-encoded-term="deere" data-term-stats="1	0.4	0.000	2251	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/deere" onclick="window.location=this.dataset.href" rel="nofollow">deere</a>
          </span>
          <span class="term-help" data-term="deere"><a href="/pebble#define=deere" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="9653" data-relevance="150" data-term="wta" data-encoded-term="wta" data-term-stats="1	0.4	0.000	9653	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/wta" onclick="window.location=this.dataset.href" rel="nofollow">wta</a>
          </span>
          <span class="term-help" data-term="wta"><a href="/pebble#define=wta" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="8142" data-relevance="149" data-term="hickory" data-encoded-term="hickory" data-term-stats="1	0.4	0.000	8142	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hickory" onclick="window.location=this.dataset.href" rel="nofollow">hickory</a>
          </span>
          <span class="term-help" data-term="hickory"><a href="/pebble#define=hickory" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1072" data-relevance="148" data-term="superspeedway" data-encoded-term="superspeedway" data-term-stats="1	0.4	0.000	1072	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/superspeedway" onclick="window.location=this.dataset.href" rel="nofollow">superspeedway</a>
          </span>
          <span class="term-help" data-term="superspeedway"><a href="/pebble#define=superspeedway" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1975" data-relevance="147" data-term="brickyard" data-encoded-term="brickyard" data-term-stats="1	0.4	0.000	1975	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/brickyard" onclick="window.location=this.dataset.href" rel="nofollow">brickyard</a>
          </span>
          <span class="term-help" data-term="brickyard"><a href="/pebble#define=brickyard" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="7540" data-relevance="146" data-term="artifact" data-encoded-term="artifact" data-term-stats="1	0.4	0.000	7540	swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/artifact" onclick="window.location=this.dataset.href" rel="nofollow">artifact</a>
          </span>
          <span class="term-help" data-term="artifact"><a href="/pebble#define=artifact" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2763" data-relevance="145" data-term="anthrax" data-encoded-term="anthrax" data-term-stats="1	0.4	0.000	2763	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/anthrax" onclick="window.location=this.dataset.href" rel="nofollow">anthrax</a>
          </span>
          <span class="term-help" data-term="anthrax"><a href="/pebble#define=anthrax" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="16644" data-relevance="144" data-term="speedway" data-encoded-term="speedway" data-term-stats="1	0.4	0.000	16644	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/speedway" onclick="window.location=this.dataset.href" rel="nofollow">speedway</a>
          </span>
          <span class="term-help" data-term="speedway"><a href="/pebble#define=speedway" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="265" data-relevance="143" data-term="medinah" data-encoded-term="medinah" data-term-stats="1	0.4	0.000	265	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/medinah" onclick="window.location=this.dataset.href" rel="nofollow">medinah</a>
          </span>
          <span class="term-help" data-term="medinah"><a href="/pebble#define=medinah" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="306" data-relevance="142" data-term="muirfield" data-encoded-term="muirfield" data-term-stats="1	0.4	0.000	306	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/muirfield" onclick="window.location=this.dataset.href" rel="nofollow">muirfield</a>
          </span>
          <span class="term-help" data-term="muirfield"><a href="/pebble#define=muirfield" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="629" data-relevance="141" data-term="raindrop" data-encoded-term="raindrop" data-term-stats="1	0.4	0.000	629	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/raindrop" onclick="window.location=this.dataset.href" rel="nofollow">raindrop</a>
          </span>
          <span class="term-help" data-term="raindrop"><a href="/pebble#define=raindrop" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="696" data-relevance="140" data-term="oakmont" data-encoded-term="oakmont" data-term-stats="1	0.4	0.000	696	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oakmont" onclick="window.location=this.dataset.href" rel="nofollow">oakmont</a>
          </span>
          <span class="term-help" data-term="oakmont"><a href="/pebble#define=oakmont" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="326" data-relevance="139" data-term="concretions" data-encoded-term="concretions" data-term-stats="1	0.4	0.000	326	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/concretions" onclick="window.location=this.dataset.href" rel="nofollow">concretions</a>
          </span>
          <span class="term-help" data-term="concretions"><a href="/pebble#define=concretions" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="511" data-relevance="138" data-term="spheroid" data-encoded-term="spheroid" data-term-stats="1	0.4	0.000	511	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spheroid" onclick="window.location=this.dataset.href" rel="nofollow">spheroid</a>
          </span>
          <span class="term-help" data-term="spheroid"><a href="/pebble#define=spheroid" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="632" data-relevance="137" data-term="indentations" data-encoded-term="indentations" data-term-stats="1	0.4	0.000	632	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/indentations" onclick="window.location=this.dataset.href" rel="nofollow">indentations</a>
          </span>
          <span class="term-help" data-term="indentations"><a href="/pebble#define=indentations" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="491" data-relevance="136" data-term="scoria" data-encoded-term="scoria" data-term-stats="1	0.4	0.000	491	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/scoria" onclick="window.location=this.dataset.href" rel="nofollow">scoria</a>
          </span>
          <span class="term-help" data-term="scoria"><a href="/pebble#define=scoria" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1227" data-relevance="135" data-term="boule" data-encoded-term="boule" data-term-stats="1	0.4	0.000	1227	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/boule" onclick="window.location=this.dataset.href" rel="nofollow">boule</a>
          </span>
          <span class="term-help" data-term="boule"><a href="/pebble#define=boule" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="358" data-relevance="134" data-term="hummock" data-encoded-term="hummock" data-term-stats="1	0.4	0.000	358	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hummock" onclick="window.location=this.dataset.href" rel="nofollow">hummock</a>
          </span>
          <span class="term-help" data-term="hummock"><a href="/pebble#define=hummock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="441" data-relevance="133" data-term="spindrift" data-encoded-term="spindrift" data-term-stats="1	0.4	0.000	441	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spindrift" onclick="window.location=this.dataset.href" rel="nofollow">spindrift</a>
          </span>
          <span class="term-help" data-term="spindrift"><a href="/pebble#define=spindrift" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="93" data-relevance="132" data-term="agates" data-encoded-term="agates" data-term-stats="1	0.4	0.000	93	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/agates" onclick="window.location=this.dataset.href" rel="nofollow">agates</a>
          </span>
          <span class="term-help" data-term="agates"><a href="/pebble#define=agates" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="309" data-relevance="131" data-term="flagstones" data-encoded-term="flagstones" data-term-stats="1	0.4	0.000	309	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flagstones" onclick="window.location=this.dataset.href" rel="nofollow">flagstones</a>
          </span>
          <span class="term-help" data-term="flagstones"><a href="/pebble#define=flagstones" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="54" data-relevance="130" data-term="dishpan" data-encoded-term="dishpan" data-term-stats="1	0.4	0.000	54	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dishpan" onclick="window.location=this.dataset.href" rel="nofollow">dishpan</a>
          </span>
          <span class="term-help" data-term="dishpan"><a href="/pebble#define=dishpan" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="855" data-relevance="129" data-term="dodecahedron" data-encoded-term="dodecahedron" data-term-stats="1	0.4	0.000	855	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dodecahedron" onclick="window.location=this.dataset.href" rel="nofollow">dodecahedron</a>
          </span>
          <span class="term-help" data-term="dodecahedron"><a href="/pebble#define=dodecahedron" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1410" data-relevance="128" data-term="macadam" data-encoded-term="macadam" data-term-stats="1	0.4	0.000	1410	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/macadam" onclick="window.location=this.dataset.href" rel="nofollow">macadam</a>
          </span>
          <span class="term-help" data-term="macadam"><a href="/pebble#define=macadam" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="785" data-relevance="127" data-term="sphagnum" data-encoded-term="sphagnum" data-term-stats="1	0.4	0.000	785	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sphagnum" onclick="window.location=this.dataset.href" rel="nofollow">sphagnum</a>
          </span>
          <span class="term-help" data-term="sphagnum"><a href="/pebble#define=sphagnum" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="409" data-relevance="126" data-term="spherically" data-encoded-term="spherically" data-term-stats="1	0.4	0.000	409	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spherically" onclick="window.location=this.dataset.href" rel="nofollow">spherically</a>
          </span>
          <span class="term-help" data-term="spherically"><a href="/pebble#define=spherically" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2567" data-relevance="125" data-term="marl" data-encoded-term="marl" data-term-stats="1	0.4	0.000	2567	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/marl" onclick="window.location=this.dataset.href" rel="nofollow">marl</a>
          </span>
          <span class="term-help" data-term="marl"><a href="/pebble#define=marl" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="900" data-relevance="124" data-term="octahedron" data-encoded-term="octahedron" data-term-stats="1	0.4	0.000	900	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/octahedron" onclick="window.location=this.dataset.href" rel="nofollow">octahedron</a>
          </span>
          <span class="term-help" data-term="octahedron"><a href="/pebble#define=octahedron" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1048" data-relevance="123" data-term="dimple" data-encoded-term="dimple" data-term-stats="1	0.4	0.000	1048	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dimple" onclick="window.location=this.dataset.href" rel="nofollow">dimple</a>
          </span>
          <span class="term-help" data-term="dimple"><a href="/pebble#define=dimple" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1245" data-relevance="122" data-term="olivine" data-encoded-term="olivine" data-term-stats="1	0.4	0.000	1245	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/olivine" onclick="window.location=this.dataset.href" rel="nofollow">olivine</a>
          </span>
          <span class="term-help" data-term="olivine"><a href="/pebble#define=olivine" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="55" data-relevance="121" data-term="pillowed" data-encoded-term="pillowed" data-term-stats="1	0.4	0.000	55	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pillowed" onclick="window.location=this.dataset.href" rel="nofollow">pillowed</a>
          </span>
          <span class="term-help" data-term="pillowed"><a href="/pebble#define=pillowed" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="420" data-relevance="120" data-term="stalactite" data-encoded-term="stalactite" data-term-stats="1	0.4	0.000	420	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stalactite" onclick="window.location=this.dataset.href" rel="nofollow">stalactite</a>
          </span>
          <span class="term-help" data-term="stalactite"><a href="/pebble#define=stalactite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="596" data-relevance="119" data-term="sawgrass" data-encoded-term="sawgrass" data-term-stats="1	0.4	0.000	596	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sawgrass" onclick="window.location=this.dataset.href" rel="nofollow">sawgrass</a>
          </span>
          <span class="term-help" data-term="sawgrass"><a href="/pebble#define=sawgrass" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1097" data-relevance="118" data-term="ridged" data-encoded-term="ridged" data-term-stats="1	0.4	0.000	1097	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ridged" onclick="window.location=this.dataset.href" rel="nofollow">ridged</a>
          </span>
          <span class="term-help" data-term="ridged"><a href="/pebble#define=ridged" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="499" data-relevance="117" data-term="shinnecock" data-encoded-term="shinnecock" data-term-stats="1	0.4	0.000	499	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/shinnecock" onclick="window.location=this.dataset.href" rel="nofollow">shinnecock</a>
          </span>
          <span class="term-help" data-term="shinnecock"><a href="/pebble#define=shinnecock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="116" data-term="geological matrix" data-encoded-term="geological%20matrix" data-term-stats="1	0.4	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/geological-matrix" onclick="window.location=this.dataset.href" rel="nofollow">geological matrix</a>
          </span>
          <span class="term-help" data-term="geological matrix"><a href="/pebble#define=geological matrix" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="754" data-relevance="115" data-term="hardcourt" data-encoded-term="hardcourt" data-term-stats="1	0.4	0.000	754	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hardcourt" onclick="window.location=this.dataset.href" rel="nofollow">hardcourt</a>
          </span>
          <span class="term-help" data-term="hardcourt"><a href="/pebble#define=hardcourt" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="729" data-relevance="114" data-term="rock genre" data-encoded-term="rock%20genre" data-term-stats="1	0.4	0.000	729	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rock-genre" onclick="window.location=this.dataset.href" rel="nofollow">rock genre</a>
          </span>
          <span class="term-help" data-term="rock genre"><a href="/pebble#define=rock genre" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1576" data-relevance="113" data-term="sedimentary rock" data-encoded-term="sedimentary%20rock" data-term-stats="1	0.4	0.000	1576	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sedimentary-rock" onclick="window.location=this.dataset.href" rel="nofollow">sedimentary rock</a>
          </span>
          <span class="term-help" data-term="sedimentary rock"><a href="/pebble#define=sedimentary rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="379" data-relevance="112" data-term="kapalua" data-encoded-term="kapalua" data-term-stats="1	0.4	0.000	379	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/kapalua" onclick="window.location=this.dataset.href" rel="nofollow">kapalua</a>
          </span>
          <span class="term-help" data-term="kapalua"><a href="/pebble#define=kapalua" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="111" data-term="find in grind" data-encoded-term="find%20in%20grind" data-term-stats="1	0.4	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/find-in-grind" onclick="window.location=this.dataset.href" rel="nofollow">find in grind</a>
          </span>
          <span class="term-help" data-term="find in grind"><a href="/pebble#define=find in grind" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="817" data-relevance="110" data-term="rock garden" data-encoded-term="rock%20garden" data-term-stats="1	0.4	0.000	817	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rock-garden" onclick="window.location=this.dataset.href" rel="nofollow">rock garden</a>
          </span>
          <span class="term-help" data-term="rock garden"><a href="/pebble#define=rock garden" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="106" data-relevance="109" data-term="baltusrol" data-encoded-term="baltusrol" data-term-stats="1	0.4	0.000	106	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/baltusrol" onclick="window.location=this.dataset.href" rel="nofollow">baltusrol</a>
          </span>
          <span class="term-help" data-term="baltusrol"><a href="/pebble#define=baltusrol" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4429" data-relevance="108" data-term="1.5-mile" data-encoded-term="1.5-mile" data-term-stats="1	0.4	0.000	4429	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/1.5-mile" onclick="window.location=this.dataset.href" rel="nofollow">1.5-mile</a>
          </span>
          <span class="term-help" data-term="1.5-mile"><a href="/pebble#define=1.5-mile" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="38746" data-relevance="107" data-term="18-hole" data-encoded-term="18-hole" data-term-stats="1	0.4	0.000	38746	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/18-hole" onclick="window.location=this.dataset.href" rel="nofollow">18-hole</a>
          </span>
          <span class="term-help" data-term="18-hole"><a href="/pebble#define=18-hole" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="62" data-relevance="106" data-term="rock flour" data-encoded-term="rock%20flour" data-term-stats="1	0.3	0.000	62	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rock-flour" onclick="window.location=this.dataset.href" rel="nofollow">rock flour</a>
          </span>
          <span class="term-help" data-term="rock flour"><a href="/pebble#define=rock flour" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="29060" data-relevance="105" data-term="tide" data-encoded-term="tide" data-term-stats="1	0.4	0.000	29060	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/tide" onclick="window.location=this.dataset.href" rel="nofollow">tide</a>
          </span>
          <span class="term-help" data-term="tide"><a href="/pebble#define=tide" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="84" data-relevance="104" data-term="oil sand" data-encoded-term="oil%20sand" data-term-stats="1	0.3	0.000	84	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oil-sand" onclick="window.location=this.dataset.href" rel="nofollow">oil sand</a>
          </span>
          <span class="term-help" data-term="oil sand"><a href="/pebble#define=oil sand" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2907" data-relevance="103" data-term="d'elegance" data-encoded-term="d'elegance" data-term-stats="1	0.3	0.000	2907	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/d'elegance" onclick="window.location=this.dataset.href" rel="nofollow">d'elegance</a>
          </span>
          <span class="term-help" data-term="d'elegance"><a href="/pebble#define=d'elegance" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="560" data-relevance="102" data-term="summerlin" data-encoded-term="summerlin" data-term-stats="1	0.3	0.000	560	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/summerlin" onclick="window.location=this.dataset.href" rel="nofollow">summerlin</a>
          </span>
          <span class="term-help" data-term="summerlin"><a href="/pebble#define=summerlin" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2935" data-relevance="101" data-term="christian rock" data-encoded-term="christian%20rock" data-term-stats="1	0.3	0.000	2935	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/christian-rock" onclick="window.location=this.dataset.href" rel="nofollow">christian rock</a>
          </span>
          <span class="term-help" data-term="christian rock"><a href="/pebble#define=christian rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="490" data-relevance="100" data-term="furyk" data-encoded-term="furyk" data-term-stats="1	0.3	0.000	490	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/furyk" onclick="window.location=this.dataset.href" rel="nofollow">furyk</a>
          </span>
          <span class="term-help" data-term="furyk"><a href="/pebble#define=furyk" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="748" data-relevance="99" data-term="oaklawn" data-encoded-term="oaklawn" data-term-stats="1	0.3	0.000	748	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oaklawn" onclick="window.location=this.dataset.href" rel="nofollow">oaklawn</a>
          </span>
          <span class="term-help" data-term="oaklawn"><a href="/pebble#define=oaklawn" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="667" data-relevance="98" data-term="kooyong" data-encoded-term="kooyong" data-term-stats="1	0.3	0.000	667	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/kooyong" onclick="window.location=this.dataset.href" rel="nofollow">kooyong</a>
          </span>
          <span class="term-help" data-term="kooyong"><a href="/pebble#define=kooyong" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="74" data-relevance="97" data-term="witchu" data-encoded-term="witchu" data-term-stats="1	0.3	0.000	74	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/witchu" onclick="window.location=this.dataset.href" rel="nofollow">witchu</a>
          </span>
          <span class="term-help" data-term="witchu"><a href="/pebble#define=witchu" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="459" data-relevance="96" data-term="turnberry" data-encoded-term="turnberry" data-term-stats="1	0.3	0.000	459	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/turnberry" onclick="window.location=this.dataset.href" rel="nofollow">turnberry</a>
          </span>
          <span class="term-help" data-term="turnberry"><a href="/pebble#define=turnberry" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="42037" data-relevance="95" data-term="9-hole" data-encoded-term="9-hole" data-term-stats="1	0.3	0.000	42037	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/9-hole" onclick="window.location=this.dataset.href" rel="nofollow">9-hole</a>
          </span>
          <span class="term-help" data-term="9-hole"><a href="/pebble#define=9-hole" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3391" data-relevance="94" data-term="lichen" data-encoded-term="lichen" data-term-stats="1	0.3	0.000	3391	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lichen" onclick="window.location=this.dataset.href" rel="nofollow">lichen</a>
          </span>
          <span class="term-help" data-term="lichen"><a href="/pebble#define=lichen" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2249" data-relevance="93" data-term="nasdaq-100" data-encoded-term="nasdaq-100" data-term-stats="1	0.3	0.000	2249	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nasdaq-100" onclick="window.location=this.dataset.href" rel="nofollow">nasdaq-100</a>
          </span>
          <span class="term-help" data-term="nasdaq-100"><a href="/pebble#define=nasdaq-100" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="11619" data-relevance="92" data-term="nine-hole" data-encoded-term="nine-hole" data-term-stats="1	0.3	0.000	11619	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nine-hole" onclick="window.location=this.dataset.href" rel="nofollow">nine-hole</a>
          </span>
          <span class="term-help" data-term="nine-hole"><a href="/pebble#define=nine-hole" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1401" data-relevance="91" data-term="cantera" data-encoded-term="cantera" data-term-stats="1	0.3	0.000	1401	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cantera" onclick="window.location=this.dataset.href" rel="nofollow">cantera</a>
          </span>
          <span class="term-help" data-term="cantera"><a href="/pebble#define=cantera" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="68" data-relevance="90" data-term="kooyonga" data-encoded-term="kooyonga" data-term-stats="1	0.3	0.000	68	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/kooyonga" onclick="window.location=this.dataset.href" rel="nofollow">kooyonga</a>
          </span>
          <span class="term-help" data-term="kooyonga"><a href="/pebble#define=kooyonga" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="268" data-relevance="89" data-term="pyroclastic flow" data-encoded-term="pyroclastic%20flow" data-term-stats="1	0.3	0.000	268	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pyroclastic-flow" onclick="window.location=this.dataset.href" rel="nofollow">pyroclastic flow</a>
          </span>
          <span class="term-help" data-term="pyroclastic flow"><a href="/pebble#define=pyroclastic flow" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="376" data-relevance="88" data-term="nedbank" data-encoded-term="nedbank" data-term-stats="1	0.3	0.000	376	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nedbank" onclick="window.location=this.dataset.href" rel="nofollow">nedbank</a>
          </span>
          <span class="term-help" data-term="nedbank"><a href="/pebble#define=nedbank" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="53" data-relevance="87" data-term="lauberhorn" data-encoded-term="lauberhorn" data-term-stats="1	0.3	0.000	53	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/lauberhorn" onclick="window.location=this.dataset.href" rel="nofollow">lauberhorn</a>
          </span>
          <span class="term-help" data-term="lauberhorn"><a href="/pebble#define=lauberhorn" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="355" data-relevance="86" data-term="hallandale" data-encoded-term="hallandale" data-term-stats="1	0.3	0.000	355	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hallandale" onclick="window.location=this.dataset.href" rel="nofollow">hallandale</a>
          </span>
          <span class="term-help" data-term="hallandale"><a href="/pebble#define=hallandale" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="57" data-relevance="85" data-term="poipu" data-encoded-term="poipu" data-term-stats="1	0.3	0.000	57	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/poipu" onclick="window.location=this.dataset.href" rel="nofollow">poipu</a>
          </span>
          <span class="term-help" data-term="poipu"><a href="/pebble#define=poipu" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="84" data-term="trioval" data-encoded-term="trioval" data-term-stats="1	0.3	0.000	-1	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/trioval" onclick="window.location=this.dataset.href" rel="nofollow">trioval</a>
          </span>
          <span class="term-help" data-term="trioval"><a href="/pebble#define=trioval" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="754" data-relevance="83" data-term="hardcourts" data-encoded-term="hardcourts" data-term-stats="1	0.3	0.000	754	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hardcourts" onclick="window.location=this.dataset.href" rel="nofollow">hardcourts</a>
          </span>
          <span class="term-help" data-term="hardcourts"><a href="/pebble#define=hardcourts" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="743" data-relevance="82" data-term="igneous rock" data-encoded-term="igneous%20rock" data-term-stats="1	0.3	0.000	743	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/igneous-rock" onclick="window.location=this.dataset.href" rel="nofollow">igneous rock</a>
          </span>
          <span class="term-help" data-term="igneous rock"><a href="/pebble#define=igneous rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1963" data-relevance="81" data-term="glf" data-encoded-term="glf" data-term-stats="1	0.3	0.000	1963	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/glf" onclick="window.location=this.dataset.href" rel="nofollow">glf</a>
          </span>
          <span class="term-help" data-term="glf"><a href="/pebble#define=glf" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2481" data-relevance="80" data-term="o'meara" data-encoded-term="o'meara" data-term-stats="1	0.3	0.000	2481	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/o'meara" onclick="window.location=this.dataset.href" rel="nofollow">o'meara</a>
          </span>
          <span class="term-help" data-term="o'meara"><a href="/pebble#define=o'meara" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="462" data-relevance="79" data-term="zapadnaya" data-encoded-term="zapadnaya" data-term-stats="1	0.3	0.000	462	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/zapadnaya" onclick="window.location=this.dataset.href" rel="nofollow">zapadnaya</a>
          </span>
          <span class="term-help" data-term="zapadnaya"><a href="/pebble#define=zapadnaya" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="7466" data-relevance="78" data-term="par-71" data-encoded-term="par-71" data-term-stats="1	0.3	0.000	7466	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/par-71" onclick="window.location=this.dataset.href" rel="nofollow">par-71</a>
          </span>
          <span class="term-help" data-term="par-71"><a href="/pebble#define=par-71" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="411" data-relevance="77" data-term="sorenstam" data-encoded-term="sorenstam" data-term-stats="1	0.3	0.000	411	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/sorenstam" onclick="window.location=this.dataset.href" rel="nofollow">sorenstam</a>
          </span>
          <span class="term-help" data-term="sorenstam"><a href="/pebble#define=sorenstam" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="141" data-relevance="76" data-term="whitethorn" data-encoded-term="whitethorn" data-term-stats="1	0.3	0.000	141	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/whitethorn" onclick="window.location=this.dataset.href" rel="nofollow">whitethorn</a>
          </span>
          <span class="term-help" data-term="whitethorn"><a href="/pebble#define=whitethorn" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="651" data-relevance="75" data-term="hootie" data-encoded-term="hootie" data-term-stats="1	0.3	0.000	651	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/hootie" onclick="window.location=this.dataset.href" rel="nofollow">hootie</a>
          </span>
          <span class="term-help" data-term="hootie"><a href="/pebble#define=hootie" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="60" data-relevance="74" data-term="rettenbach" data-encoded-term="rettenbach" data-term-stats="1	0.3	0.000	60	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rettenbach" onclick="window.location=this.dataset.href" rel="nofollow">rettenbach</a>
          </span>
          <span class="term-help" data-term="rettenbach"><a href="/pebble#define=rettenbach" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3233" data-relevance="73" data-term="2.5-mile" data-encoded-term="2.5-mile" data-term-stats="1	0.3	0.000	3233	w2v	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/2.5-mile" onclick="window.location=this.dataset.href" rel="nofollow">2.5-mile</a>
          </span>
          <span class="term-help" data-term="2.5-mile"><a href="/pebble#define=2.5-mile" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="72" data-term="shovelfuls" data-encoded-term="shovelfuls" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/shovelfuls" onclick="window.location=this.dataset.href" rel="nofollow">shovelfuls</a>
          </span>
          <span class="term-help" data-term="shovelfuls"><a href="/pebble#define=shovelfuls" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="71" data-term="waterworn" data-encoded-term="waterworn" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/waterworn" onclick="window.location=this.dataset.href" rel="nofollow">waterworn</a>
          </span>
          <span class="term-help" data-term="waterworn"><a href="/pebble#define=waterworn" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="476" data-relevance="70" data-term="whitecap" data-encoded-term="whitecap" data-term-stats="1	0.3	0.000	476	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/whitecap" onclick="window.location=this.dataset.href" rel="nofollow">whitecap</a>
          </span>
          <span class="term-help" data-term="whitecap"><a href="/pebble#define=whitecap" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="69" data-term="glasslike" data-encoded-term="glasslike" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/glasslike" onclick="window.location=this.dataset.href" rel="nofollow">glasslike</a>
          </span>
          <span class="term-help" data-term="glasslike"><a href="/pebble#define=glasslike" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="68" data-term="spadeful" data-encoded-term="spadeful" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spadeful" onclick="window.location=this.dataset.href" rel="nofollow">spadeful</a>
          </span>
          <span class="term-help" data-term="spadeful"><a href="/pebble#define=spadeful" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="269" data-relevance="67" data-term="slickrock" data-encoded-term="slickrock" data-term-stats="1	0.3	0.000	269	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/slickrock" onclick="window.location=this.dataset.href" rel="nofollow">slickrock</a>
          </span>
          <span class="term-help" data-term="slickrock"><a href="/pebble#define=slickrock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="55" data-relevance="66" data-term="posthole" data-encoded-term="posthole" data-term-stats="1	0.3	0.000	55	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/posthole" onclick="window.location=this.dataset.href" rel="nofollow">posthole</a>
          </span>
          <span class="term-help" data-term="posthole"><a href="/pebble#define=posthole" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="127" data-relevance="65" data-term="corrugations" data-encoded-term="corrugations" data-term-stats="1	0.3	0.000	127	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/corrugations" onclick="window.location=this.dataset.href" rel="nofollow">corrugations</a>
          </span>
          <span class="term-help" data-term="corrugations"><a href="/pebble#define=corrugations" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="305" data-relevance="64" data-term="geode" data-encoded-term="geode" data-term-stats="1	0.3	0.000	305	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/geode" onclick="window.location=this.dataset.href" rel="nofollow">geode</a>
          </span>
          <span class="term-help" data-term="geode"><a href="/pebble#define=geode" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="63" data-term="wetly" data-encoded-term="wetly" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/wetly" onclick="window.location=this.dataset.href" rel="nofollow">wetly</a>
          </span>
          <span class="term-help" data-term="wetly"><a href="/pebble#define=wetly" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="62" data-term="snowlike" data-encoded-term="snowlike" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/snowlike" onclick="window.location=this.dataset.href" rel="nofollow">snowlike</a>
          </span>
          <span class="term-help" data-term="snowlike"><a href="/pebble#define=snowlike" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="150" data-relevance="61" data-term="pontil" data-encoded-term="pontil" data-term-stats="1	0.3	0.000	150	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pontil" onclick="window.location=this.dataset.href" rel="nofollow">pontil</a>
          </span>
          <span class="term-help" data-term="pontil"><a href="/pebble#define=pontil" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="60" data-term="saltshaker" data-encoded-term="saltshaker" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/saltshaker" onclick="window.location=this.dataset.href" rel="nofollow">saltshaker</a>
          </span>
          <span class="term-help" data-term="saltshaker"><a href="/pebble#define=saltshaker" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="116" data-relevance="59" data-term="gumdrop" data-encoded-term="gumdrop" data-term-stats="1	0.3	0.000	116	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gumdrop" onclick="window.location=this.dataset.href" rel="nofollow">gumdrop</a>
          </span>
          <span class="term-help" data-term="gumdrop"><a href="/pebble#define=gumdrop" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="394" data-relevance="58" data-term="spherules" data-encoded-term="spherules" data-term-stats="1	0.3	0.000	394	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/spherules" onclick="window.location=this.dataset.href" rel="nofollow">spherules</a>
          </span>
          <span class="term-help" data-term="spherules"><a href="/pebble#define=spherules" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="57" data-term="squashy" data-encoded-term="squashy" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/squashy" onclick="window.location=this.dataset.href" rel="nofollow">squashy</a>
          </span>
          <span class="term-help" data-term="squashy"><a href="/pebble#define=squashy" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="151" data-relevance="56" data-term="planetesimal" data-encoded-term="planetesimal" data-term-stats="1	0.3	0.000	151	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/planetesimal" onclick="window.location=this.dataset.href" rel="nofollow">planetesimal</a>
          </span>
          <span class="term-help" data-term="planetesimal"><a href="/pebble#define=planetesimal" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="55" data-term="indention" data-encoded-term="indention" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/indention" onclick="window.location=this.dataset.href" rel="nofollow">indention</a>
          </span>
          <span class="term-help" data-term="indention"><a href="/pebble#define=indention" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="838" data-relevance="54" data-term="maile" data-encoded-term="maile" data-term-stats="1	0.3	0.000	838	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/maile" onclick="window.location=this.dataset.href" rel="nofollow">maile</a>
          </span>
          <span class="term-help" data-term="maile"><a href="/pebble#define=maile" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5521" data-relevance="53" data-term="very hard" data-encoded-term="very%20hard" data-term-stats="1	0.3	0.000	5521	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/very-hard" onclick="window.location=this.dataset.href" rel="nofollow">very hard</a>
          </span>
          <span class="term-help" data-term="very hard"><a href="/pebble#define=very hard" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="52" data-term="kerbstone" data-encoded-term="kerbstone" data-term-stats="1	0.3	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/kerbstone" onclick="window.location=this.dataset.href" rel="nofollow">kerbstone</a>
          </span>
          <span class="term-help" data-term="kerbstone"><a href="/pebble#define=kerbstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="66" data-relevance="51" data-term="gobstopper" data-encoded-term="gobstopper" data-term-stats="1	0.3	0.000	66	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gobstopper" onclick="window.location=this.dataset.href" rel="nofollow">gobstopper</a>
          </span>
          <span class="term-help" data-term="gobstopper"><a href="/pebble#define=gobstopper" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="22159" data-relevance="50" data-term="rock music" data-encoded-term="rock%20music" data-term-stats="1	0.3	0.000	22159	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rock-music" onclick="window.location=this.dataset.href" rel="nofollow">rock music</a>
          </span>
          <span class="term-help" data-term="rock music"><a href="/pebble#define=rock music" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="471" data-relevance="49" data-term="glob" data-encoded-term="glob" data-term-stats="1	0.3	0.000	471	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/glob" onclick="window.location=this.dataset.href" rel="nofollow">glob</a>
          </span>
          <span class="term-help" data-term="glob"><a href="/pebble#define=glob" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="48" data-term="wentworth scale" data-encoded-term="wentworth%20scale" data-term-stats="1	0.3	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/wentworth-scale" onclick="window.location=this.dataset.href" rel="nofollow">wentworth scale</a>
          </span>
          <span class="term-help" data-term="wentworth scale"><a href="/pebble#define=wentworth scale" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="47" data-term="pave stone" data-encoded-term="pave%20stone" data-term-stats="1	0.3	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pave-stone" onclick="window.location=this.dataset.href" rel="nofollow">pave stone</a>
          </span>
          <span class="term-help" data-term="pave stone"><a href="/pebble#define=pave stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="323" data-relevance="46" data-term="rock crystal" data-encoded-term="rock%20crystal" data-term-stats="1	0.3	0.000	323	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rock-crystal" onclick="window.location=this.dataset.href" rel="nofollow">rock crystal</a>
          </span>
          <span class="term-help" data-term="rock crystal"><a href="/pebble#define=rock crystal" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="165" data-relevance="45" data-term="stone curlew" data-encoded-term="stone%20curlew" data-term-stats="1	0.3	0.000	165	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stone-curlew" onclick="window.location=this.dataset.href" rel="nofollow">stone curlew</a>
          </span>
          <span class="term-help" data-term="stone curlew"><a href="/pebble#define=stone curlew" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="44" data-term="drag bite" data-encoded-term="drag%20bite" data-term-stats="1	0.3	0.000	-1	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/drag-bite" onclick="window.location=this.dataset.href" rel="nofollow">drag bite</a>
          </span>
          <span class="term-help" data-term="drag bite"><a href="/pebble#define=drag bite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="62" data-relevance="43" data-term="stone crab" data-encoded-term="stone%20crab" data-term-stats="1	0.3	0.000	62	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/stone-crab" onclick="window.location=this.dataset.href" rel="nofollow">stone crab</a>
          </span>
          <span class="term-help" data-term="stone crab"><a href="/pebble#define=stone crab" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1821" data-relevance="42" data-term="ice cube" data-encoded-term="ice%20cube" data-term-stats="1	0.2	0.000	1821	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ice-cube" onclick="window.location=this.dataset.href" rel="nofollow">ice cube</a>
          </span>
          <span class="term-help" data-term="ice cube"><a href="/pebble#define=ice cube" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="15609" data-relevance="41" data-term="estuary" data-encoded-term="estuary" data-term-stats="1	0.3	0.000	15609	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/estuary" onclick="window.location=this.dataset.href" rel="nofollow">estuary</a>
          </span>
          <span class="term-help" data-term="estuary"><a href="/pebble#define=estuary" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="11472" data-relevance="40" data-term="river ore" data-encoded-term="river%20ore" data-term-stats="1	0.2	0.000	11472	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/river-ore" onclick="window.location=this.dataset.href" rel="nofollow">river ore</a>
          </span>
          <span class="term-help" data-term="river ore"><a href="/pebble#define=river ore" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1088" data-relevance="39" data-term="volcanic rock" data-encoded-term="volcanic%20rock" data-term-stats="1	0.2	0.000	1088	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/volcanic-rock" onclick="window.location=this.dataset.href" rel="nofollow">volcanic rock</a>
          </span>
          <span class="term-help" data-term="volcanic rock"><a href="/pebble#define=volcanic rock" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="62" data-relevance="38" data-term="flower petal" data-encoded-term="flower%20petal" data-term-stats="1	0.1	0.000	62	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/flower-petal" onclick="window.location=this.dataset.href" rel="nofollow">flower petal</a>
          </span>
          <span class="term-help" data-term="flower petal"><a href="/pebble#define=flower petal" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="188" data-relevance="37" data-term="mud puddle" data-encoded-term="mud%20puddle" data-term-stats="1	0.1	0.000	188	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/mud-puddle" onclick="window.location=this.dataset.href" rel="nofollow">mud puddle</a>
          </span>
          <span class="term-help" data-term="mud puddle"><a href="/pebble#define=mud puddle" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="144" data-relevance="36" data-term="banana peel" data-encoded-term="banana%20peel" data-term-stats="1	0.1	0.000	144	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/banana-peel" onclick="window.location=this.dataset.href" rel="nofollow">banana peel</a>
          </span>
          <span class="term-help" data-term="banana peel"><a href="/pebble#define=banana peel" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="35" data-term="chamois cloth" data-encoded-term="chamois%20cloth" data-term-stats="1	0.1	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/chamois-cloth" onclick="window.location=this.dataset.href" rel="nofollow">chamois cloth</a>
          </span>
          <span class="term-help" data-term="chamois cloth"><a href="/pebble#define=chamois cloth" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="50" data-relevance="34" data-term="darning needle" data-encoded-term="darning%20needle" data-term-stats="1	0.1	0.000	50	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/darning-needle" onclick="window.location=this.dataset.href" rel="nofollow">darning needle</a>
          </span>
          <span class="term-help" data-term="darning needle"><a href="/pebble#define=darning needle" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1573" data-relevance="33" data-term="oyster shell" data-encoded-term="oyster%20shell" data-term-stats="1	0.1	0.000	1573	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/oyster-shell" onclick="window.location=this.dataset.href" rel="nofollow">oyster shell</a>
          </span>
          <span class="term-help" data-term="oyster shell"><a href="/pebble#define=oyster shell" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="32" data-term="vein quartz" data-encoded-term="vein%20quartz" data-term-stats="1	0.1	0.000	-1	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/vein-quartz" onclick="window.location=this.dataset.href" rel="nofollow">vein quartz</a>
          </span>
          <span class="term-help" data-term="vein quartz"><a href="/pebble#define=vein quartz" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1570" data-relevance="31" data-term="ant hill" data-encoded-term="ant%20hill" data-term-stats="1	0.1	0.000	1570	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ant-hill" onclick="window.location=this.dataset.href" rel="nofollow">ant hill</a>
          </span>
          <span class="term-help" data-term="ant hill"><a href="/pebble#define=ant hill" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="36157" data-relevance="30" data-term="nasa" data-encoded-term="nasa" data-term-stats="1	0.0	0.000	36157	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/nasa" onclick="window.location=this.dataset.href" rel="nofollow">nasa</a>
          </span>
          <span class="term-help" data-term="nasa"><a href="/pebble#define=nasa" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="5850" data-relevance="29" data-term="landscaping" data-encoded-term="landscaping" data-term-stats="1	0.1	0.000	5850	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/landscaping" onclick="window.location=this.dataset.href" rel="nofollow">landscaping</a>
          </span>
          <span class="term-help" data-term="landscaping"><a href="/pebble#define=landscaping" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="10034" data-relevance="28" data-term="curiosity" data-encoded-term="curiosity" data-term-stats="1	0.0	0.000	10034	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/curiosity" onclick="window.location=this.dataset.href" rel="nofollow">curiosity</a>
          </span>
          <span class="term-help" data-term="curiosity"><a href="/pebble#define=curiosity" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="58760" data-relevance="27" data-term="mars" data-encoded-term="mars" data-term-stats="1	0.0	0.000	58760	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/mars" onclick="window.location=this.dataset.href" rel="nofollow">mars</a>
          </span>
          <span class="term-help" data-term="mars"><a href="/pebble#define=mars" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="144845" data-relevance="26" data-term="israel" data-encoded-term="israel" data-term-stats="1	0.0	0.000	144845	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/israel" onclick="window.location=this.dataset.href" rel="nofollow">israel</a>
          </span>
          <span class="term-help" data-term="israel"><a href="/pebble#define=israel" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1009" data-relevance="25" data-term="norwegian sea" data-encoded-term="norwegian%20sea" data-term-stats="1	-0.1	0.000	1009	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/norwegian-sea" onclick="window.location=this.dataset.href" rel="nofollow">norwegian sea</a>
          </span>
          <span class="term-help" data-term="norwegian sea"><a href="/pebble#define=norwegian sea" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="371" data-relevance="24" data-term="bookend" data-encoded-term="bookend" data-term-stats="1	-0.1	0.000	371	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/bookend" onclick="window.location=this.dataset.href" rel="nofollow">bookend</a>
          </span>
          <span class="term-help" data-term="bookend"><a href="/pebble#define=bookend" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="187" data-relevance="23" data-term="paperweight" data-encoded-term="paperweight" data-term-stats="1	-0.1	0.000	187	wiki|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/paperweight" onclick="window.location=this.dataset.href" rel="nofollow">paperweight</a>
          </span>
          <span class="term-help" data-term="paperweight"><a href="/pebble#define=paperweight" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="387" data-relevance="22" data-term="halite" data-encoded-term="halite" data-term-stats="1	-0.1	0.000	387	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/halite" onclick="window.location=this.dataset.href" rel="nofollow">halite</a>
          </span>
          <span class="term-help" data-term="halite"><a href="/pebble#define=halite" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="103940" data-relevance="21" data-term="water current" data-encoded-term="water%20current" data-term-stats="1	-0.2	0.000	103940	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/water-current" onclick="window.location=this.dataset.href" rel="nofollow">water current</a>
          </span>
          <span class="term-help" data-term="water current"><a href="/pebble#define=water current" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="3020" data-relevance="20" data-term="dead sea" data-encoded-term="dead%20sea" data-term-stats="1	-0.3	0.000	3020	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/dead-sea" onclick="window.location=this.dataset.href" rel="nofollow">dead sea</a>
          </span>
          <span class="term-help" data-term="dead sea"><a href="/pebble#define=dead sea" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="163382" data-relevance="19" data-term="building construction" data-encoded-term="building%20construction" data-term-stats="1	-0.3	0.000	163382	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/building-construction" onclick="window.location=this.dataset.href" rel="nofollow">building construction</a>
          </span>
          <span class="term-help" data-term="building construction"><a href="/pebble#define=building construction" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="739" data-relevance="18" data-term="ecological niche" data-encoded-term="ecological%20niche" data-term-stats="1	-0.3	0.000	739	swiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/ecological-niche" onclick="window.location=this.dataset.href" rel="nofollow">ecological niche</a>
          </span>
          <span class="term-help" data-term="ecological niche"><a href="/pebble#define=ecological niche" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1962" data-relevance="17" data-term="pet rocks" data-encoded-term="pet%20rocks" data-term-stats="1	-0.3	0.000	1962	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pet-rocks" onclick="window.location=this.dataset.href" rel="nofollow">pet rocks</a>
          </span>
          <span class="term-help" data-term="pet rocks"><a href="/pebble#define=pet rocks" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="13978" data-relevance="16" data-term="comet" data-encoded-term="comet" data-term-stats="undefined	0.0	0.000	13978	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/comet" onclick="window.location=this.dataset.href" rel="nofollow">comet</a>
          </span>
          <span class="term-help" data-term="comet"><a href="/pebble#define=comet" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2310" data-relevance="15" data-term="blob" data-encoded-term="blob" data-term-stats="0	1.4	0.000	2310	vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/blob" onclick="window.location=this.dataset.href" rel="nofollow">blob</a>
          </span>
          <span class="term-help" data-term="blob"><a href="/pebble#define=blob" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="-1" data-relevance="14" data-term="pearl" data-encoded-term="pearl" data-term-stats="undefined	0.0	0.000	-1	undefined	undefined">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pearl" onclick="window.location=this.dataset.href" rel="nofollow">pearl</a>
          </span>
          <span class="term-help" data-term="pearl"><a href="/pebble#define=pearl" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="61080" data-relevance="13" data-term="rocks" data-encoded-term="rocks" data-term-stats="1	0.8	0.000	61080	ol|reverse-net|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/rocks" onclick="window.location=this.dataset.href" rel="nofollow">rocks</a>
          </span>
          <span class="term-help" data-term="rocks"><a href="/pebble#define=rocks" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="573443" data-relevance="12" data-term="river" data-encoded-term="river" data-term-stats="1	0.7	0.000	573443	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/river" onclick="window.location=this.dataset.href" rel="nofollow">river</a>
          </span>
          <span class="term-help" data-term="river"><a href="/pebble#define=river" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="844" data-relevance="11" data-term="seashell" data-encoded-term="seashell" data-term-stats="1	0.4	0.000	844	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/seashell" onclick="window.location=this.dataset.href" rel="nofollow">seashell</a>
          </span>
          <span class="term-help" data-term="seashell"><a href="/pebble#define=seashell" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="1711" data-relevance="10" data-term="gemstone" data-encoded-term="gemstone" data-term-stats="1	0.7	0.000	1711	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gemstone" onclick="window.location=this.dataset.href" rel="nofollow">gemstone</a>
          </span>
          <span class="term-help" data-term="gemstone"><a href="/pebble#define=gemstone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="2645" data-relevance="9" data-term="starfish" data-encoded-term="starfish" data-term-stats="1	0.6	0.000	2645	ol|vec2	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/starfish" onclick="window.location=this.dataset.href" rel="nofollow">starfish</a>
          </span>
          <span class="term-help" data-term="starfish"><a href="/pebble#define=starfish" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="14880" data-relevance="8" data-term="gem" data-encoded-term="gem" data-term-stats="1	0.6	0.000	14880	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/gem" onclick="window.location=this.dataset.href" rel="nofollow">gem</a>
          </span>
          <span class="term-help" data-term="gem"><a href="/pebble#define=gem" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="134" data-relevance="7" data-term="cabochon" data-encoded-term="cabochon" data-term-stats="1	0.6	0.000	134	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/cabochon" onclick="window.location=this.dataset.href" rel="nofollow">cabochon</a>
          </span>
          <span class="term-help" data-term="cabochon"><a href="/pebble#define=cabochon" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="189482" data-relevance="6" data-term="beach" data-encoded-term="beach" data-term-stats="1	0.4	0.000	189482	w2v|reverse-net	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/beach" onclick="window.location=this.dataset.href" rel="nofollow">beach</a>
          </span>
          <span class="term-help" data-term="beach"><a href="/pebble#define=beach" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="33673" data-relevance="5" data-term="mineral" data-encoded-term="mineral" data-term-stats="1	0.4	0.000	33673	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/mineral" onclick="window.location=this.dataset.href" rel="nofollow">mineral</a>
          </span>
          <span class="term-help" data-term="mineral"><a href="/pebble#define=mineral" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="399" data-relevance="4" data-term="precious stone" data-encoded-term="precious%20stone" data-term-stats="1	0.3	0.000	399	cn5	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/precious-stone" onclick="window.location=this.dataset.href" rel="nofollow">precious stone</a>
          </span>
          <span class="term-help" data-term="precious stone"><a href="/pebble#define=precious stone" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="4034" data-relevance="3" data-term="seawater" data-encoded-term="seawater" data-term-stats="1	0.3	0.000	4034	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/seawater" onclick="window.location=this.dataset.href" rel="nofollow">seawater</a>
          </span>
          <span class="term-help" data-term="seawater"><a href="/pebble#define=seawater" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="56" data-relevance="2" data-term="smoky quartz" data-encoded-term="smoky%20quartz" data-term-stats="1	0.1	0.000	56	ol	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/smoky-quartz" onclick="window.location=this.dataset.href" rel="nofollow">smoky quartz</a>
          </span>
          <span class="term-help" data-term="smoky quartz"><a href="/pebble#define=smoky quartz" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="25765" data-relevance="1" data-term="pacific ocean" data-encoded-term="pacific%20ocean" data-term-stats="1	-0.1	0.000	25765	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/pacific-ocean" onclick="window.location=this.dataset.href" rel="nofollow">pacific ocean</a>
          </span>
          <span class="term-help" data-term="pacific ocean"><a href="/pebble#define=pacific ocean" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li><li data-frequency="150" data-relevance="0" data-term="wind wave" data-encoded-term="wind%20wave" data-term-stats="1	-0.2	0.000	150	wiki	1">
        <div class="word-ctn">
          <span class="term">
            <a href="#" data-href="/wind-wave" onclick="window.location=this.dataset.href" rel="nofollow">wind wave</a>
          </span>
          <span class="term-help" data-term="wind wave"><a href="/pebble#define=wind wave" style="display: none;">&amp;nbsp;</a></span>
        </div>
        <div class="vote-ctn">
          <div class="upvote vote-btn" data-dir="1"></div>
          <div class="downvote vote-btn" data-dir="-1"></div>
        </div>
      </li>
      </ul>
"""

# Parse the HTML using the built-in html.parser
soup = BeautifulSoup(html, 'html.parser')

# Find all elements that have the "data-encoded-term" attribute
elements = soup.find_all(attrs={"data-encoded-term": True})

# Extract the values of data-encoded-term attributes
data_encoded_terms = [el['data-encoded-term'] for el in elements]

print(data_encoded_terms)
