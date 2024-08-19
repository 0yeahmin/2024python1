import  wikipedia
# wiki=wikipedia.page('Artificial intelligence')
# text=wiki.content
text="lawyer, Slack served in the Missouri General Assembly from 1842 to 1843 and saw combat in the Mexican–American War. After the outbreak of the American Civil War in April 1861, Slack, who held pro-slavery views, supported the Confederate cause. When the Missouri State Guard was formed the next month to oppose the Union Army, he was appointed as a brigadier general, commanding its 4th Division. After participating in the Battle of Carthage in July, he fought in the Battle of Wilson's Creek on August 10, where he suffered a bad "
print(text)
from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()
# 김민서(7반)
