
#Filtering for students who'se first college is Evergreen Valley
evc_cohort = final_df.loc[(final_df['College Code/Branch'] =='012452-00') & (final_df['College Sequence'] ==1)]

#Filtering for students that transferred to a 4-year institution
transfers = final_df.loc[(final_df['2-year / 4-year'] == "4") & (final_df['College Sequence'] ==2)]


evc_transfers = transfers.loc[transfers["Requester Return Field"].isin(evc_cohort["Requester Return Field"])]


colleges = evc_transfers.groupby(['College Name'], as_index=False)["Requester Return Field"].agg('count')

top_colleges = colleges.sort_values(['Requester Return Field'], ascending = False)[:10]

print(top_colleges)
