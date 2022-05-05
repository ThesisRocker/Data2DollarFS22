{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7f676af2-d552-42da-b30f-add5c0a52bfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "CRITICAL:root:twint.get:User:'NoneType' object is not subscriptable\n",
      "CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0)\n",
      "sleeping for 1.0 secs\n",
      "CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0)\n",
      "sleeping for 8.0 secs\n",
      "CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0)\n",
      "sleeping for 27.0 secs\n",
      "CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0)\n",
      "sleeping for 64.0 secs\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/run.py\u001b[0m in \u001b[0;36mFeed\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     64\u001b[0m                 \u001b[0;32melif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTwitterSearch\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 65\u001b[0;31m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfeed\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minit\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfeed\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mJson\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     66\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/feed.py\u001b[0m in \u001b[0;36mJson\u001b[0;34m(response)\u001b[0m\n\u001b[1;32m     41\u001b[0m     \u001b[0mlogme\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m':Json'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 42\u001b[0;31m     \u001b[0mjson_response\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mloads\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     43\u001b[0m     \u001b[0mhtml\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mjson_response\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"items_html\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/json/__init__.py\u001b[0m in \u001b[0;36mloads\u001b[0;34m(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[1;32m    356\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[0;32m--> 357\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    358\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/json/decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[0;34m(self, s, _w)\u001b[0m\n\u001b[1;32m    336\u001b[0m         \"\"\"\n\u001b[0;32m--> 337\u001b[0;31m         \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/json/decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[0;34m(self, s, idx)\u001b[0m\n\u001b[1;32m    354\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 355\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Expecting value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    356\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-205bacf302d9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;31m# Run\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m \u001b[0mtwint\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSearch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/run.py\u001b[0m in \u001b[0;36mSearch\u001b[0;34m(config, callback)\u001b[0m\n\u001b[1;32m    325\u001b[0m     \u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mProfile\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    326\u001b[0m     \u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mProfile_full\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 327\u001b[0;31m     \u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcallback\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    328\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mPandas_au\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    329\u001b[0m         \u001b[0mstorage\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpanda\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_autoget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"tweet\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/run.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(config, callback)\u001b[0m\n\u001b[1;32m    224\u001b[0m         \u001b[0;32mraise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    225\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 226\u001b[0;31m     \u001b[0mget_event_loop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun_until_complete\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mTwint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcallback\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    227\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    228\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mFavorites\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/nest_asyncio.py\u001b[0m in \u001b[0;36mrun_until_complete\u001b[0;34m(self, future)\u001b[0m\n\u001b[1;32m     62\u001b[0m                 \u001b[0mf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_log_destroy_pending\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     63\u001b[0m             \u001b[0;32mwhile\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdone\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 64\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_run_once\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     65\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_stopping\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     66\u001b[0m                     \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/nest_asyncio.py\u001b[0m in \u001b[0;36m_run_once\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     98\u001b[0m             \u001b[0mhandle\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mready\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpopleft\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     99\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mhandle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_cancelled\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 100\u001b[0;31m                 \u001b[0mhandle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_run\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    101\u001b[0m         \u001b[0mhandle\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/asyncio/events.py\u001b[0m in \u001b[0;36m_run\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     79\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_run\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 81\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_context\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_callback\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_args\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     82\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mSystemExit\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     83\u001b[0m             \u001b[0;32mraise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/nest_asyncio.py\u001b[0m in \u001b[0;36mstep\u001b[0;34m(task, exc)\u001b[0m\n\u001b[1;32m    167\u001b[0m         \u001b[0mcurr_task\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcurr_tasks\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_loop\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    168\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 169\u001b[0;31m             \u001b[0mstep_orig\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtask\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    170\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    171\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mcurr_task\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/asyncio/tasks.py\u001b[0m in \u001b[0;36m__step\u001b[0;34m(***failed resolving arguments***)\u001b[0m\n\u001b[1;32m    278\u001b[0m                 \u001b[0;31m# We use the `send` method directly, because coroutines\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    279\u001b[0m                 \u001b[0;31m# don't have `__iter__` and `__next__` methods.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 280\u001b[0;31m                 \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcoro\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    281\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    282\u001b[0m                 \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcoro\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mthrow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mexc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/run.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    175\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mUntil\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0md\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_until\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    176\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfeed\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 177\u001b[0;31m                     \u001b[0;32mawait\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtweets\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    178\u001b[0m                 \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    179\u001b[0m                     \u001b[0mlogme\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m':Twint:main:gettingNewTweets'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/run.py\u001b[0m in \u001b[0;36mtweets\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    135\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    136\u001b[0m     \u001b[0;32masync\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mtweets\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 137\u001b[0;31m         \u001b[0;32mawait\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mFeed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    138\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mLocation\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    139\u001b[0m             \u001b[0mlogme\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m':Twint:tweets:location'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/twint/run.py\u001b[0m in \u001b[0;36mFeed\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     96\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     97\u001b[0m                     \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstderr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'sleeping for {} secs\\n'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdelay\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 98\u001b[0;31m                     \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdelay\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     99\u001b[0m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser_agent\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mawait\u001b[0m \u001b[0mget\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mRandomUserAgent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwa\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    100\u001b[0m                     \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "#prevent run time error\n",
    "import nest_asyncio\n",
    "nest_asyncio.apply()\n",
    "\n",
    "import twint\n",
    "\n",
    "# Configure\n",
    "c = twint.Config()\n",
    "#User\n",
    "c.Username = \"ABack\"\n",
    "#timeframe\n",
    "c.Since = \"2010-01-01\"\n",
    "c.Until = \"2022-03-09\"\n",
    "#Output\n",
    "c.Output = \"ElazarBrief.json\"\n",
    "\n",
    "# Run\n",
    "twint.run.Search(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f257e176-2016-4354-8d42-c1ff0e6637ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
