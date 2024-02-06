import pandas as pd
import numpy as np

df = pd.read_excel('dax_impression_delivery.xlsm')


currency_columns_to_add = [("payout_adv_payout_USD", "payout_adv_payout", "currency_rates_USD"),
                           ("payout_adv_payout_GBP", "payout_adv_payout", "currency_rates_GBP"),
                           ("payout_adv_payout_CAD", "payout_adv_payout", "currency_rates_CAD"),
                           ("payout_adv_payout_EUR", "payout_adv_payout", "currency_rates_EUR"),
                           ("payout_pub_payout_USD", "payout_pub_payout", "currency_rates_USD"),
                           ("payout_pub_payout_GBP", "payout_pub_payout", "currency_rates_GBP"),
                           ("payout_pub_payout_CAD", "payout_pub_payout", "currency_rates_CAD"),
                           ("payout_pub_payout_EUR", "payout_pub_payout", "currency_rates_EUR"),
                           ("payout_sp_payout_USD", "payout_sp_payout", "currency_rates_USD"),
                           ("payout_sp_payout_GBP", "payout_sp_payout", "currency_rates_GBP"),
                           ("payout_sp_payout_CAD", "payout_sp_payout", "currency_rates_CAD"),
                           ("payout_sp_payout_EUR", "payout_sp_payout", "currency_rates_EUR")]

cols_to_cast = [
    ("click_event_time", "LongType()"),
    ("imp_event_time", "LongType()"),
    ("click_event_time", "LongType()"),
    ("complete_event_time", "LongType()"),
    ("agency_commission_percentage", "DoubleType()"),
    ("show_spot_rev_share_percentage", "DoubleType()"),
    ("show_spot_cpm_GBP", "DoubleType()"),
    ("show_prog_cpm_GBP", "DoubleType()"),
    ("show_sponsorship_rev_share_percentage", "DoubleType()"),
    ("show_host_read_rev_share_percentage", "DoubleType()"),
    ("show_host_read_cpm_GBP", "DoubleType()"),
    ("publisher_spot_rev_share_percentage", "DoubleType()"),
    ("publisher_spot_cpm_GBP", "DoubleType()"),
    ("publisher_prog_cpm_GBP", "DoubleType()"),
    ("publisher_sponsorship_rev_share_percentage", "DoubleType()"),
    ("publisher_host_read_rev_share_percentage", "DoubleType()"),
    ("publisher_host_read_cpm_GBP", "DoubleType()"),
]

cols_to_rename = [("impression_time", "ad_request_time"),
                  ("showid", "show_id"),
                  ("supply_provider_tagid", "supply_provider_tag_id"),
                  ("publisher_ad_unit_id", "channel_id"),
                  ("line_item_id", "ad_id"),
                  ("line_item_category_list", "ad_category_list"),
                  ("line_item_is_frontloaded", "ad_is_frontloaded"),
                  ("line_item_pricing_type", "ad_pricing_type"),
                  ("campaign_order_id", "order_id"),
                  ("deal_id", "deal_external_id"),
                  ("deal_internal_id", "deal_id"),
                  ("dsp_landing_page_domain", "advertiser_domain"),
                  ("line_item_tags", "ad_tags")
                  ]

vast_columns_to_add = [
    ("is_imp", 0),
    ("is_click", 0),
    ("payout_adv_payout_USD", 0.0),
    ("payout_adv_payout_GBP", 0.0),
    ("payout_adv_payout_CAD", 0.0),
    ("payout_adv_payout_EUR", 0.0),
    ("payout_pub_payout_USD", 0.0),
    ("payout_pub_payout_GBP", 0.0),
    ("payout_pub_payout_CAD", 0.0),
    ("payout_pub_payout_EUR", 0.0),
    ("payout_sp_payout_USD", 0.0),
    ("payout_sp_payout_GBP", 0.0),
    ("payout_sp_payout_CAD", 0.0),
    ("payout_sp_payout_EUR", 0.0),
    ("click_event_time", None),
    ("imp_event_time", None),
    ("agency_commission_percentage", None),
    ("show_spot_rev_share_percentage", None),
    ("show_spot_cpm_GBP", None),
    ("show_prog_cpm_GBP", None),
    ("show_sponsorship_rev_share_percentage", None),
    ("show_host_read_rev_share_percentage", None),
    ("show_host_read_cpm_GBP", None),
    ("publisher_spot_rev_share_percentage", None),
    ("publisher_spot_cpm_GBP", None),
    ("publisher_prog_cpm_GBP", None),
    ("publisher_sponsorship_rev_share_percentage", None),
    ("publisher_host_read_rev_share_percentage", None),
    ("publisher_host_read_cpm_GBP", None),
    ("platform_spot_rev_net_USD", 0.0),
    ("platform_spot_rev_net_GBP", 0.0),
    ("platform_spot_rev_net_CAD", 0.0),
    ("platform_spot_rev_net_EUR", 0.0),
    ("publisher_spot_rev_net_USD", 0.0),
    ("publisher_spot_rev_net_GBP", 0.0),
    ("publisher_spot_rev_net_CAD", 0.0),
    ("publisher_spot_rev_net_EUR", 0.0),
    ("is_deferred", 0),
    ("is_dynamic", 0),
    ("is_host_read", 0),
    ("is_listener_id", 0),
    ("is_partner_sold", 0),
    ("is_podcast_specific", 0),
    ("is_sponsorship", 0),
    ("is_fixed", 0),
    ("is_targeted", 0),
    ("is_value", 0),
    ("is_filler", 0),
    ("is_sold", 0),
    ("is_unsold", 0),
    ("platform_spon_rev_net_GBP", 0.0),
    ("platform_spon_rev_net_EUR", 0.0),
    ("platform_spon_rev_net_CAD", 0.0),
    ("platform_spon_rev_net_USD", 0.0),
    ("publisher_spon_rev_net_GBP", 0.0),
    ("publisher_spon_rev_net_EUR", 0.0),
    ("publisher_spon_rev_net_CAD", 0.0),
    ("publisher_spon_rev_net_USD", 0.0)
]

vast_indicators_to_add = [("is_vast_midpoint", "midpoint"), ("is_vast_thirdQuartile", "thirdQuartile"),
                          ("is_vast_complete", "complete"), ("is_vast_start", "start"),
                          ("is_vast_firstQuartile", "firstQuartile"), ("is_vast_skip", "skip"),
                          ("is_vast_rewind", "rewind"), ("is_vast_resume", "resume"),
                          ("is_vast_pause", "pause"), ("is_vast_unmute", "unmute"), ("is_vast_mute", "mute")]

custom_function_cols_vast = [("ad_request_time", 'f.col("ad_request_time").cast(LongType()) * 1000'),
                                 ("is_direct", 'f.when(f.col("campaign_id").isNotNull(), True).otherwise(False)'),
                                 ("agency_id", 'f.when(f.col("advertiser_agency_id").isNull(), f.col("bid_agency_id")).otherwise( f.col("advertiser_agency_id"))'),
                                 ("is_vast_creativeView", 'f.when((f.col("is_imp") == 0) & (f.col("is_click") == 0) & (f.col("companion_ad_id").isNull()) &  (f.col("name") == "creativeView"), 1).otherwise(f.lit(0))'),
                                 ("is_companion_impression", 'f.when((f.col("companion_ad_id").isNotNull()) & (f.col("name") == "creativeView"), 1).otherwise(0)')
                             ]
df["new_column"] = ""
df["transformation"] = ""
for i in currency_columns_to_add:
    for index, row in df.iterrows():
        if row['COLUMN_NAME'].lower() == i[0].lower():
            df.loc[index, "new_column"] = "Vast_Calculation"
            df.loc[index, "transformation"] = f"round({i[1]} * {i[2]}, 14)"
            print("Row Index:", index, "Value:", row['COLUMN_NAME'])

for j in cols_to_cast:
    for index, row in df.iterrows():
        if row['COLUMN_NAME'].lower() == j[0].lower():
            df.loc[index, "new_column"] = "Vast_Calculation"
            df.loc[index, "transformation"] = f"cast({j[1]})"
            print("Row Index:", index, "Value:", row['COLUMN_NAME'])

for k in cols_to_rename:
    for index, row in df.iterrows():
       if row['COLUMN_NAME'].lower() == k[1].lower():
            df.loc[index, "new_column"] = "Vast"
            #df.loc[index, "transformation"] = f"cast({i[1]})"
            #print("Row Index:", index, "Value:", row['COLUMN_NAME'])

        #print("Index:", index, "Value:", value)

for m in vast_columns_to_add:
    for index, row in df.iterrows():
        if row['COLUMN_NAME'].lower() == m[0].lower():
            df.loc[index, "new_column"] = "Vast"
            if row["transformation"] != "":
                df.loc[index, "transformation"] = f"{row['transformation']} + default({m[1]})"
            else:
                df.loc[index, "transformation"] = f"default({m[1]})"
            #print("Row Index:", index, "Value:", row['COLUMN_NAME'])

for n in vast_indicators_to_add:
    for index, row in df.iterrows():
        if row['COLUMN_NAME'].lower() == n[0].lower():
            df.loc[index, "new_column"] = "Vast"
            if row["transformation"] != "":
                df.loc[index, "transformation"] = f"{row['transformation']} + if column_in_vast(name) == {n[1]} than 1 else 0"
            else:
                df.loc[index, "transformation"] = f"if column_in_vast(name) == {n[1]} than 1 else 0"

for l in custom_function_cols_vast:
    for index, row in df.iterrows():
        if row['COLUMN_NAME'].lower() == l[0].lower():
            df.loc[index, "new_column"] = "Vast"
            if row["transformation"] != "":
                df.loc[index, "transformation"] = f"{row['transformation']} +  {l[1]} "
            else:
                df.loc[index, "transformation"] = f"{l[1]} "

df.to_excel("output.xlsx")
#print(dataframe1)