Specific Catalyst Cost ($/ton
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/tsql_kpi.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/tsql_kpi.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Specific%20Catalyst%20Cost%20%28%24/ton" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Specific Catalyst Cost measures the cost of catalyst used per ton of product produced</li><li>providing insight into the efficiency and economic viability of the catalyst utilization in production processes</li><li>Cost of catalyst consumed per ton of product</li><li>used to monitor and optimize catalyst usage</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of tracking Specific Catalyst Cost is to optimize catalyst usage and reduce overall production costs</li><li>thereby enhancing profitability and operational efficiency</li><li>Control catalyst spend while maintaining performance and product quality</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The formula for Specific Catalyst Cost is derived by dividing the total catalyst cost by the total product tons produced, ensuring that the cost is accurately allocated per unit of output.</p>
               <div class="math-equation">$$ \mathrm{Catalyst\,Cost\,per\,Ton} = \frac{\mathrm{Catalyst\,Cost}}{\mathrm{Product\,Tons}} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               50.3s (AI 50.3s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 50.278s
                  • AI: 50.278s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is utilized in performance assessments related to catalyst efficiency</li><li>cost management</li><li>and overall production economics</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the total catalyst cost incurred during production and the total tons of product produced</li><li>Catalyst cost used and product tons over the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Specific Catalyst Cost is expressed in dollars per ton.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI typically includes financial records and production data from operational databases.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Monitoring Specific Catalyst Cost is crucial for identifying trends in catalyst expenses and making informed decisions regarding catalyst selection and usage strategies.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Specific Catalyst Cost ($/ton)
   -- Formula: \mathrm{Catalyst\,Cost\,per\,Ton} = \frac{\mathrm{Catalyst\,Cost}}{\mathrm{Product\,Tons}}

   -- T-SQL example KPI calculation
   SELECT CAST(catalyst_cost / NULLIF(product_tons, 0) AS DECIMAL(18,6)) AS kpi_specific_catalyst_cost;